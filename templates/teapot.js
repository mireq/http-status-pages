(function() {

var canvas, gl, lineShader;
var time = 0;


function makeShaderProgram(vs, fs) {
	function attachShader(type, code) {
		var shader = gl.createShader(type);
		gl.shaderSource(shader, code);
		gl.compileShader(shader);
		if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
			throw "Shader not compiled:\n" + gl.getShaderInfoLog(shader);
		}
		gl.attachShader(program, shader);
	}

	var program = gl.createProgram();
	attachShader(gl.VERTEX_SHADER, vs);
	attachShader(gl.FRAGMENT_SHADER, fs);
	gl.linkProgram(program);
	if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
		throw "Program not linked:\n" + gl.getProgramInfoLog(program);
	}
	return program;
}


function makeArrayBuffer(items) {
	var buf = gl.createBuffer();
	gl.bindBuffer(gl.ARRAY_BUFFER, buf);
	gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(items), gl.STATIC_DRAW);
	return buf;
}

function attributeLocation(name) {
	return gl.getAttribLocation(lineShader, name);
}

function uniformLocation(name) {
	return gl.getUniformLocation(lineShader, name);
}

function initGl() {
	canvas = document.createElement('canvas');
	canvas.className = 'background-canvas';
	document.body.insertBefore(canvas, document.body.firstChild);

	gl = canvas.getContext("webgl", {antialias: false}) || canvas.getContext("experimental-webgl");
	if (!gl) {
		document.body.removeChild(canvas);
		return false;
	}

	lineShader = makeShaderProgram(
"attribute vec3 pos;\n"+
"uniform float vw;\n"+
"uniform float vh;\n"+
"uniform float z_near;\n"+
"uniform float z_far;\n"+
"uniform float fovy;\n"+
"uniform vec3 center;\n"+
"uniform vec3 eye;\n"+
"uniform vec3 up;\n"+
"uniform int offset;\n"+
"mat4 perspective() {\n"+
"	float zmul = (-2.0 * z_near * z_far) / (z_far - z_near);\n"+
"	float ymul = 1.0 / tan(fovy * 3.14159265 / 360.0);\n"+
"	float xmul = ymul / (vw / vh);\n"+
"	return mat4(\n"+
"		xmul, 0.0, 0.0, 0.0,\n"+
"		0.0, ymul, 0.0, 0.0,\n"+
"		0.0, 0.0, -1.0, -1.0,\n"+
"		0.0, 0.0, zmul, 0.0\n"+
"	);\n"+
"}\n"+
"mat4 lookat() {\n"+
"	vec3 forward = normalize(center - eye);\n"+
"	vec3 side = normalize(cross(forward, up));\n"+
"	vec3 upward = cross(side, forward);\n"+
"	return mat4(\n"+
"		side.x, upward.x, -forward.x, 0,\n"+
"		side.y, upward.y, -forward.y, 0,\n"+
"		side.z, upward.z, -forward.z, 0,\n"+
"		-dot(eye, side), -dot(eye, upward), dot(eye, forward), 1\n"+
"	);\n"+
"}\n"+
"void main() {\n"+
"	gl_Position = perspective() * lookat() * vec4(pos, 1.0) + vec4(0.0, float(offset) / vh * 2.0, 0.0, 0.0);\n"+
"}\n",
"uniform mediump vec4 out_color;\n"+
"void main() {\n"+
"	gl_FragColor = out_color;\n"+
"	gl_FragColor.a = clamp((0.4 + (0.95 - gl_FragCoord.z) * 8.0), 0.0, 1.0) * gl_FragColor.a;\n"+
"	gl_FragColor.rgb *= gl_FragColor.a;\n"+
"}\n"
	);

	var modelBuffer = makeArrayBuffer(model);

	// Bind model to shader
	var attr = attributeLocation("pos");
	gl.enableVertexAttribArray(attr);
	gl.vertexAttribPointer(attr, 3, gl.FLOAT, false, 0, 0);

	return true;
}



function render() {
	gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);

	gl.clearColor(0.0, 0.0, 0.0, 0.0);
	gl.clear(gl.COLOR_BUFFER_BIT);

	time += 0.05;

	attr = uniformLocation("out_color");
	gl.uniform4f(attr, 0.0, 0.0, 0.0, 0.07);
	attr = uniformLocation("offset");
	gl.uniform1i(attr, 0);
	attr = uniformLocation("eye");
	gl.uniform3f(attr, Math.sin(time / 31) * 2.0 * (Math.sin(time / 67) * 0.5 + 1), Math.sin(time / 83) * 1.0, Math.cos(time / 31) * 2.0 * (Math.sin(time / 67) * 0.5 + 1));
	attr = uniformLocation("up");
	gl.uniform3f(attr, Math.sin(time / 149) * 0.5, -1.0, 0.0);

	gl.useProgram(lineShader);

	gl.drawArrays(gl.LINES, 0, model.length / 3);

	attr = uniformLocation("out_color");
	gl.uniform4f(attr, 1.0, 1.0, 1.0, 0.2);
	attr = uniformLocation("offset");
	gl.uniform1i(attr, 1);

	gl.drawArrays(gl.LINES, 0, model.length / 3);

	requestAnimationFrame(render);
}


function resizeCanvas() {
	if (canvas.width == canvas.clientWidth && canvas.height == canvas.clientHeight) {
		return;
	}
	var width = canvas.clientWidth;
	var height = canvas.clientHeight;
	var max = Math.max(width, height);
	var maxSize = Math.min(max, 4096);
	var scale = maxSize / max;
	width = Math.round(width * scale);
	height = Math.round(height * scale);
	canvas.width = width;
	canvas.height = height;

	gl.useProgram(lineShader);
	var attr;
	attr = uniformLocation("vw");
	gl.uniform1f(attr, canvas.clientWidth);
	attr = uniformLocation("vh");
	gl.uniform1f(attr, canvas.clientHeight);
	attr = uniformLocation("z_near");
	gl.uniform1f(attr, 0.1);
	attr = uniformLocation("z_far");
	gl.uniform1f(attr, 10.0);
	attr = uniformLocation("fovy");
	gl.uniform1f(attr, 40.0);
	attr = uniformLocation("center");
	gl.uniform3f(attr, 0.0, -0.7, 0.0);
	attr = uniformLocation("up");
	gl.uniform3f(attr, 0.0, 1.0, 0.0);
}


if (!initGl()) {
	return;
}

resizeCanvas();


requestAnimationFrame(render);
document.body.onresize = resizeCanvas;


}());
