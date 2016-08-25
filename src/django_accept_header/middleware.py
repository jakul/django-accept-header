# -*- coding: utf-8 -*-
# Copyright (c) 2015, Michael Fladischer <michael@fladi.at>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from __future__ import absolute_import

from django import http

from .exceptions import ParsingError
from .header import parse


class AcceptMiddleware(object):

    def process_request(self, request):
        try:
            acc = parse(request.META.get('HTTP_ACCEPT'))
        except ParsingError:
            return http.HttpResponseBadRequest()
        setattr(request, 'accepted_types', acc)
        request.accepts = lambda mt: any(ma.matches(mt) for ma in acc)
