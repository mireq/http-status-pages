# -*- coding: utf-8 -*-

# Data from http://webconcepts.info/concepts/http-status-code.json

HTTP_CODES = [
	{ "value" : "100",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/100",
		"description" : "Continue",
		"details" :
		[
			{ "description" : "The 100 (Continue) status code indicates that the initial part of a request has been received and has not yet been rejected by the server. The server intends to send a final response after the request has been fully received and acted upon.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.2.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "101",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/101",
		"description" : "Switching Protocols",
		"details" :
		[
			{ "description" : "The 101 (Switching Protocols) status code indicates that the server understands and is willing to comply with the client's request, via the Upgrade header field, for a change in the application protocol being used on this connection. The server MUST generate an Upgrade header field in the response that indicates which protocol(s) will be switched to immediately after the empty line that terminates the 101 response.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.2.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "102",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/102",
		"description" : "Processing",
		"details" :
		[
			{ "description" : "The 102 (Processing) status code is an interim response used to inform the client that the server has accepted the complete request, but has not yet completed it. This status code SHOULD only be sent when the server has a reasonable expectation that the request will take significant time to complete. As guidance, if a method is taking longer than 20 seconds (a reasonable, but arbitrary value) to process the server SHOULD return a 102 (Processing) response. The server MUST send a final response after the request has been completed.",
				"documentation" : "http://tools.ietf.org/html/rfc2518#section-10.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/2518",
				"spec-name" : "RFC 2518" } ] },

	{ "value" : "103",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/103",
		"description" : "Early Hints",
		"details" :
		[
			{ "description" : "The 103 (Early Hints) status code indicates the client that the server is likely to send a final request with the headers included in the informational response.",
				"documentation" : "http://tools.ietf.org/html/rfc8297#section-2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/8297",
				"spec-name" : "RFC 8297" } ] },

	{ "value" : "200",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/200",
		"description" : "OK",
		"details" :
		[
			{ "description" : "The 200 (OK) status code indicates that the request has succeeded. The payload sent in a 200 response depends on the request method.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.3.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "201",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/201",
		"description" : "Created",
		"details" :
		[
			{ "description" : "The 201 (Created) status code indicates that the request has been fulfilled and has resulted in one or more new resources being created. The primary resource created by the request is identified by either a Location header field in the response or, if no Location field is received, by the effective request URI.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.3.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "202",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/202",
		"description" : "Accepted",
		"details" :
		[
			{ "description" : "The 202 (Accepted) status code indicates that the request has been accepted for processing, but the processing has not been completed. The request might or might not eventually be acted upon, as it might be disallowed when processing actually takes place. There is no facility in HTTP for re-sending a status code from an asynchronous operation.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.3.3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "203",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/203",
		"description" : "Non-Authoritative Information",
		"details" :
		[
			{ "description" : "The 203 (Non-Authoritative Information) status code indicates that the request was successful but the enclosed payload has been modified from that of the origin server's 200 (OK) response by a transforming proxy.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.3.4",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "204",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/204",
		"description" : "No Content",
		"details" :
		[
			{ "description" : "The 204 (No Content) status code indicates that the server has successfully fulfilled the request and that there is no additional content to send in the response payload body. Metadata in the response header fields refer to the target resource and its selected representation after the requested action was applied.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.3.5",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "205",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/205",
		"description" : "Reset Content",
		"details" :
		[
			{ "description" : "The 205 (Reset Content) status code indicates that the server has fulfilled the request and desires that the user agent reset the \"document view\", which caused the request to be sent, to its original state as received from the origin server.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.3.6",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "206",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/206",
		"description" : "Partial Content",
		"details" :
		[
			{ "description" : "The 206 (Partial Content) status code indicates that the server is successfully fulfilling a range request for the target resource by transferring one or more parts of the selected representation that correspond to the satisfiable ranges found in the request's Range header field.",
				"documentation" : "http://tools.ietf.org/html/rfc7233#section-4.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7233",
				"spec-name" : "RFC 7233" } ] },

	{ "value" : "207",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/207",
		"description" : "Multi-Status",
		"details" :
		[
			{ "description" : "The 207 (Multi-Status) status code provides status for multiple independent operations.",
				"documentation" : "http://tools.ietf.org/html/rfc4918#section-11.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/4918",
				"spec-name" : "RFC 4918" } ] },

	{ "value" : "208",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/208",
		"description" : "Already Reported",
		"details" :
		[
			{ "description" : "The 208 (Already Reported) status code can be used inside a DAV: propstat response element to avoid enumerating the internal members of multiple bindings to the same collection repeatedly. For each binding to a collection inside the request's scope, only one will be reported with a 200 status, while subsequent DAV:response elements for all other bindings will use the 208 status, and no DAV:response elements for their descendants are included.",
				"documentation" : "http://tools.ietf.org/html/rfc5842#section-7.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/5842",
				"spec-name" : "RFC 5842" } ] },

	{ "value" : "226",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/226",
		"description" : "IM Used",
		"details" :
		[
			{ "description" : "The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance. The actual current instance might not be available except by combining this response with other previous or future responses, as appropriate for the specific instance-manipulation(s).",
				"documentation" : "http://tools.ietf.org/html/rfc3229#section-10.4.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/3229",
				"spec-name" : "RFC 3229" } ] },

	{ "value" : "300",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/300",
		"description" : "Multiple Choices",
		"details" :
		[
			{ "description" : "The 300 (Multiple Choices) status code indicates that the target resource has more than one representation, each with its own more specific identifier, and information about the alternatives is being provided so that the user (or user agent) can select a preferred representation by redirecting its request to one or more of those identifiers. In other words, the server desires that the user agent engage in reactive negotiation to select the most appropriate representation(s) for its needs.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.4.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "301",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/301",
		"description" : "Moved Permanently",
		"details" :
		[
			{ "description" : "The 301 (Moved Permanently) status code indicates that the target resource has been assigned a new permanent URI and any future references to this resource ought to use one of the enclosed URIs. Clients with link-editing capabilities ought to automatically re-link references to the effective request URI to one or more of the new references sent by the server, where possible.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.4.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "302",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/302",
		"description" : "Found",
		"details" :
		[
			{ "description" : "The 302 (Found) status code indicates that the target resource resides temporarily under a different URI. Since the redirection might be altered on occasion, the client ought to continue to use the effective request URI for future requests.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.4.3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "303",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/303",
		"description" : "See Other",
		"details" :
		[
			{ "description" : "The 303 (See Other) status code indicates that the server is redirecting the user agent to a different resource, as indicated by a URI in the Location header field, which is intended to provide an indirect response to the original request. A user agent can perform a retrieval request targeting that URI (a GET or HEAD request if using HTTP), which might also be redirected, and present the eventual result as an answer to the original request. Note that the new URI in the Location header field is not considered equivalent to the effective request URI.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.4.4",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "304",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/304",
		"description" : "Not Modified",
		"details" :
		[
			{ "description" : "The 304 (Not Modified) status code indicates that a conditional GET or HEAD request has been received and would have resulted in a 200 (OK) response if it were not for the fact that the condition evaluated to false. In other words, there is no need for the server to transfer a representation of the target resource because the request indicates that the client, which made the request conditional, already has a valid representation; the server is therefore redirecting the client to make use of that stored representation as if it were the payload of a 200 (OK) response.",
				"documentation" : "http://tools.ietf.org/html/rfc7232#section-4.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7232",
				"spec-name" : "RFC 7232" } ] },

	{ "value" : "305",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/305",
		"description" : "Use Proxy",
		"details" :
		[
			{ "description" : "The 305 (Use Proxy) status code was defined in a previous version of HTTP/1.1 and is now deprecated.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.4.5",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "306",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/306",
		"description" : "Unused",
		"details" :
		[
			{ "description" : "The 306 status code was defined in a previous version of HTTP/1.1, is no longer used, and the code is reserved.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.4.6",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "307",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/307",
		"description" : "Temporary Redirect",
		"details" :
		[
			{ "description" : "The 307 (Temporary Redirect) status code indicates that the target resource resides temporarily under a different URI and the user agent MUST NOT change the request method if it performs an automatic redirection to that URI. Since the redirection can change over time, the client ought to continue using the original effective request URI for future requests.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.4.7",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "308",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/308",
		"description" : "Permanent Redirect",
		"details" :
		[
			{ "description" : "The 308 (Permanent Redirect) status code indicates that the target resource has been assigned a new permanent URI and any future references to this resource ought to use one of the enclosed URIs.",
				"documentation" : "http://tools.ietf.org/html/rfc7538#section-3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7538",
				"spec-name" : "RFC 7538" } ] },

	{ "value" : "400",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/400",
		"description" : "Bad Request",
		"details" :
		[
			{ "description" : "The 400 (Bad Request) status code indicates that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "401",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/401",
		"description" : "Unauthorized",
		"details" :
		[
			{ "description" : "The 401 (Unauthorized) status code indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. The server generating a 401 response MUST send a WWW-Authenticate header field (Section 4.1) containing at least one challenge applicable to the target resource.",
				"documentation" : "http://tools.ietf.org/html/rfc7235#section-3.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7235",
				"spec-name" : "RFC 7235" } ] },

	{ "value" : "402",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/402",
		"description" : "Payment Required",
		"details" :
		[
			{ "description" : "The 402 (Payment Required) status code is reserved for future use.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "403",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/403",
		"description" : "Forbidden",
		"details" :
		[
			{ "description" : "The 403 (Forbidden) status code indicates that the server understood the request but refuses to authorize it. A server that wishes to make public why the request has been forbidden can describe that reason in the response payload (if any).",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "404",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/404",
		"description" : "Not Found",
		"details" :
		[
			{ "description" : "The 404 (Not Found) status code indicates that the origin server did not find a current representation for the target resource or is not willing to disclose that one exists. A 404 status code does not indicate whether this lack of representation is temporary or permanent; the 410 (Gone) status code is preferred over 404 if the origin server knows, presumably through some configurable means, that the condition is likely to be permanent.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.4",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "405",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/405",
		"description" : "Method Not Allowed",
		"details" :
		[
			{ "description" : "The 405 (Method Not Allowed) status code indicates that the method received in the request-line is known by the origin server but not supported by the target resource. The origin server MUST generate an Allow header field in a 405 response containing a list of the target resource's currently supported methods.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.5",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "406",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/406",
		"description" : "Not Acceptable",
		"details" :
		[
			{ "description" : "The 406 (Not Acceptable) status code indicates that the target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.6",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "407",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/407",
		"description" : "Proxy Authentication Required",
		"details" :
		[
			{ "description" : "The 407 (Proxy Authentication Required) status code is similar to 401 (Unauthorized), but it indicates that the client needs to authenticate itself in order to use a proxy. The proxy MUST send a Proxy-Authenticate header field containing a challenge applicable to that proxy for the target resource. The client MAY repeat the request with a new or replaced Proxy-Authorization header field.",
				"documentation" : "http://tools.ietf.org/html/rfc7235#section-3.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7235",
				"spec-name" : "RFC 7235" } ] },

	{ "value" : "408",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/408",
		"description" : "Request Timeout",
		"details" :
		[
			{ "description" : "The 408 (Request Timeout) status code indicates that the server did not receive a complete request message within the time that it was prepared to wait. A server SHOULD send the \"close\" connection option in the response, since 408 implies that the server has decided to close the connection rather than continue waiting. If the client has an outstanding request in transit, the client MAY repeat that request on a new connection.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.7",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "409",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/409",
		"description" : "Conflict",
		"details" :
		[
			{ "description" : "The 409 (Conflict) status code indicates that the request could not be completed due to a conflict with the current state of the target resource. This code is used in situations where the user might be able to resolve the conflict and resubmit the request. The server SHOULD generate a payload that includes enough information for a user to recognize the source of the conflict.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.8",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "410",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/410",
		"description" : "Gone",
		"details" :
		[
			{ "description" : "The 410 (Gone) status code indicates that access to the target resource is no longer available at the origin server and that this condition is likely to be permanent. If the origin server does not know, or has no facility to determine, whether or not the condition is permanent, the status code 404 (Not Found) ought to be used instead.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.9",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "411",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/411",
		"description" : "Length Required",
		"details" :
		[
			{ "description" : "The 411 (Length Required) status code indicates that the server refuses to accept the request without a defined Content-Length. The client MAY repeat the request if it adds a valid Content-Length header field containing the length of the message body in the request message.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.10",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "412",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/412",
		"description" : "Precondition Failed",
		"details" :
		[
			{ "description" : "The 412 (Precondition Failed) status code indicates that one or more conditions given in the request header fields evaluated to false when tested on the server. This response code allows the client to place preconditions on the current resource state (its current representations and metadata) and, thus, prevent the request method from being applied if the target resource is in an unexpected state.",
				"documentation" : "http://tools.ietf.org/html/rfc7232#section-4.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7232",
				"spec-name" : "RFC 7232" } ] },

	{ "value" : "413",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/413",
		"description" : "Payload Too Large",
		"details" :
		[
			{ "description" : "The 413 (Payload Too Large) status code indicates that the server is refusing to process a request because the request payload is larger than the server is willing or able to process. The server MAY close the connection to prevent the client from continuing the request.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.11",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "414",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/414",
		"description" : "URI Too Long",
		"details" :
		[
			{ "description" : "The 414 (URI Too Long) status code indicates that the server is refusing to service the request because the request-target is longer than the server is willing to interpret.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.12",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "415",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/415",
		"description" : "Unsupported Media Type",
		"details" :
		[
			{ "description" : "The 415 (Unsupported Media Type) status code indicates that the origin server is refusing to service the request because the payload is in a format not supported by this method on the target resource. The format problem might be due to the request's indicated Content-Type or Content-Encoding, or as a result of inspecting the data directly.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.13",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "416",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/416",
		"description" : "Range Not Satisfiable",
		"details" :
		[
			{ "description" : "The 416 (Range Not Satisfiable) status code indicates that none of the ranges in the request's Range header field (Section 3.1) overlap the current extent of the selected resource or that the set of ranges requested has been rejected due to invalid ranges or an excessive request of small or overlapping ranges.",
				"documentation" : "http://tools.ietf.org/html/rfc7233#section-4.4",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7233",
				"spec-name" : "RFC 7233" } ] },

	{ "value" : "417",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/417",
		"description" : "Expectation Failed",
		"details" :
		[
			{ "description" : "The 417 (Expectation Failed) status code indicates that the expectation given in the request's Expect header field could not be met by at least one of the inbound servers.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.14",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "418",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/418",
		"description" : "I'm a teapot",
		"details" :
		[
			{ "description" : "Any attempt to brew coffee with a teapot should result in the error code \"418 I'm a teapot\". The resulting entity body MAY be short and stout.",
				"documentation" : "http://tools.ietf.org/html/rfc2324#section-2.3.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/2324",
				"spec-name" : "RFC 2324" } ] },

	{ "value" : "421",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/421",
		"description" : "Misdirected Request",
		"details" :
		[
			{ "description" : "The 421 (Misdirected Request) status code indicates that the request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.",
				"documentation" : "http://tools.ietf.org/html/rfc7540#section-9.1.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7540",
				"spec-name" : "RFC 7540" } ] },

	{ "value" : "422",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/422",
		"description" : "Unprocessable Entity",
		"details" :
		[
			{ "description" : "The 422 (Unprocessable Entity) status code means the server understands the content type of the request entity (hence a 415 (Unsupported Media Type) status code is inappropriate), and the syntax of the request entity is correct (thus a 400 (Bad Request) status code is inappropriate) but was unable to process the contained instructions. For example, this error condition may occur if an XML request body contains well-formed (i.e., syntactically correct), but semantically erroneous, XML instructions.",
				"documentation" : "http://tools.ietf.org/html/rfc4918#section-11.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/4918",
				"spec-name" : "RFC 4918" } ] },

	{ "value" : "423",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/423",
		"description" : "Locked",
		"details" :
		[
			{ "description" : "The 423 (Locked) status code means the source or destination resource of a method is locked. This response SHOULD contain an appropriate precondition or postcondition code, such as 'lock-token-submitted' or 'no-conflicting-lock'.",
				"documentation" : "http://tools.ietf.org/html/rfc4918#section-11.3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/4918",
				"spec-name" : "RFC 4918" } ] },

	{ "value" : "424",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/424",
		"description" : "Failed Dependency",
		"details" :
		[
			{ "description" : "The 424 (Failed Dependency) status code means that the method could not be performed on the resource because the requested action depended on another action and that action failed. For example, if a command in a PROPPATCH method fails, then, at minimum, the rest of the commands will also fail with 424 (Failed Dependency).",
				"documentation" : "http://tools.ietf.org/html/rfc4918#section-11.4",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/4918",
				"spec-name" : "RFC 4918" } ] },

	{ "value" : "425",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/425",
		"description" : "Too Early",
		"details" :
		[
			{ "description" : "A 425 (Too Early) status code indicates that the server is unwilling to risk processing a request that might be replayed. User agents that send a request in early data are expected to retry the request when receiving a 425 (Too Early) response status code. A user agent SHOULD retry automatically, but any retries MUST NOT be sent in early data.",
				"documentation" : "http://tools.ietf.org/html/rfc8470#section-5.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/8470",
				"spec-name" : "RFC 8470" } ] },

	{ "value" : "426",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/426",
		"description" : "Upgrade Required",
		"details" :
		[
			{ "description" : "The 426 (Upgrade Required) status code indicates that the server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server MUST send an Upgrade header field in a 426 response to indicate the required protocol(s).",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.5.15",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "428",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/428",
		"description" : "Precondition Required",
		"details" :
		[
			{ "description" : "The 428 status code indicates that the origin server requires the request to be conditional.",
				"documentation" : "http://tools.ietf.org/html/rfc6585#section-3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/6585",
				"spec-name" : "RFC 6585" } ] },

	{ "value" : "429",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/429",
		"description" : "Too Many Requests",
		"details" :
		[
			{ "description" : "The 429 status code indicates that the user has sent too many requests in a given amount of time (\"rate limiting\").",
				"documentation" : "http://tools.ietf.org/html/rfc6585#section-4",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/6585",
				"spec-name" : "RFC 6585" } ] },

	{ "value" : "431",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/431",
		"description" : "Request Header Fields Too Large",
		"details" :
		[
			{ "description" : "The 431 status code indicates that the server is unwilling to process the request because its header fields are too large. The request MAY be resubmitted after reducing the size of the request header fields.",
				"documentation" : "http://tools.ietf.org/html/rfc6585#section-5",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/6585",
				"spec-name" : "RFC 6585" } ] },

	{ "value" : "451",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/451",
		"description" : "Unavailable For Legal Reasons",
		"details" :
		[
			{ "description" : "This status code indicates that the server is denying access to the resource as a consequence of a legal demand. The server in question might not be an origin server. This type of legal demand typically most directly affects the operations of ISPs and search engines.",
				"documentation" : "http://tools.ietf.org/html/rfc7725#section-3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7725",
				"spec-name" : "RFC 7725" } ] },

	{ "value" : "497",
		"concept" : "https://http.dev/497",
		"id" : "https://http.dev/497",
		"description" : "HTTP Request Sent to HTTPS Port",
		"details" :
		[
			{ "description" : "This status code is used by some proxies or servers (not standardized) to indicate that an HTTP request was received on a port that requires HTTPS. The client should retry the request using HTTPS instead of HTTP.",
				"documentation" : "https://http.dev/497",
				"specification" : "https://http.dev/497",
				"spec-name" : "Unofficial HTTP Status Codes" } ] },

	{ "value" : "500",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/500",
		"description" : "Internal Server Error",
		"details" :
		[
			{ "description" : "The 500 (Internal Server Error) status code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.6.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "501",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/501",
		"description" : "Not Implemented",
		"details" :
		[
			{ "description" : "The 501 (Not Implemented) status code indicates that the server does not support the functionality required to fulfill the request. This is the appropriate response when the server does not recognize the request method and is not capable of supporting it for any resource.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.6.2",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "502",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/502",
		"description" : "Bad Gateway",
		"details" :
		[
			{ "description" : "The 502 (Bad Gateway) status code indicates that the server, while acting as a gateway or proxy, received an invalid response from an inbound server it accessed while attempting to fulfill the request.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.6.3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "503",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/503",
		"description" : "Service Unavailable",
		"details" :
		[
			{ "description" : "The 503 (Service Unavailable) status code indicates that the server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. The server MAY send a Retry-After header field to suggest an appropriate amount of time for the client to wait before retrying the request.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.6.4",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "504",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/504",
		"description" : "Gateway Timeout",
		"details" :
		[
			{ "description" : "The 504 (Gateway Timeout) status code indicates that the server, while acting as a gateway or proxy, did not receive a timely response from an upstream server it needed to access in order to complete the request.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.6.5",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "505",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/505",
		"description" : "HTTP Version Not Supported",
		"details" :
		[
			{ "description" : "The 505 (HTTP Version Not Supported) status code indicates that the server does not support, or refuses to support, the major version of HTTP that was used in the request message. The server is indicating that it is unable or unwilling to complete the request using the same major version as the client, other than with this error message. The server SHOULD generate a representation for the 505 response that describes why that version is not supported and what other protocols are supported by that server.",
				"documentation" : "http://tools.ietf.org/html/rfc7231#section-6.6.6",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/7231",
				"spec-name" : "RFC 7231" } ] },

	{ "value" : "506",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/506",
		"description" : "Variant Also Negotiates",
		"details" :
		[
			{ "description" : "The 506 status code indicates that the server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.",
				"documentation" : "http://tools.ietf.org/html/rfc7725#section-3",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/2295",
				"spec-name" : "RFC 2295" } ] },

	{ "value" : "507",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/507",
		"description" : "Insufficient Storage",
		"details" :
		[
			{ "description" : "The 507 (Insufficient Storage) status code means the method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request. This condition is considered to be temporary. If the request that received this status code was the result of a user action, the request MUST NOT be repeated until it is requested by a separate user action.",
				"documentation" : "http://tools.ietf.org/html/rfc4918#section-11.5",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/4918",
				"spec-name" : "RFC 4918" } ] },

	{ "value" : "508",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/508",
		"description" : "Loop Detected",
		"details" :
		[
			{ "description" : "The 508 (Loop Detected) status code indicates that the server terminated an operation because it encountered an infinite loop while processing a request with \"Depth: infinity\". This status indicates that the entire operation failed.",
				"documentation" : "http://tools.ietf.org/html/rfc5842#section-7.1",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/5842",
				"spec-name" : "RFC 5842" } ] },

	{ "value" : "510",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/510",
		"description" : "Not Extended",
		"details" :
		[
			{ "description" : "The policy for accessing the resource has not been met in the request. The server should send back all the information necessary for the client to issue an extended request. It is outside the scope of this specification to specify how the extensions inform the client.",
				"documentation" : "http://tools.ietf.org/html/rfc2774#section-7",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/2774",
				"spec-name" : "RFC 2774" } ] },

	{ "value" : "511",
		"concept" : "http://webconcepts.info/concepts/http-status-code/",
		"id" : "http://webconcepts.info/concepts/http-status-code/511",
		"description" : "Network Authentication Required",
		"details" :
		[
			{ "description" : "The 511 status code indicates that the client needs to authenticate to gain network access.",
				"documentation" : "http://tools.ietf.org/html/rfc6585#section-6",
				"specification" : "http://webconcepts.info/specs/IETF/RFC/6585",
				"spec-name" : "RFC 6585" } ] } ]
