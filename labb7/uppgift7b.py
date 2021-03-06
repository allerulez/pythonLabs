#Anton Gefvert antge210, Aleksi Evansson aleev379
#7. Abstraktion
#Uppgift 7b


#----- SPANS -----
def new_time_spans():
    " -> time_spans"
    return attach_tag('time_spans', [])

def is_time_spans(object):
    "Python-object -> Bool"
    return get_tag(object) == 'time_spans'

def is_empty_time_spans(spans):
    "time_spans -> Bool"
    ensure(spans, is_time_spans)
    return not strip_tag(spans)

def insert_time_span(span, spans):
    "span x time_spans -> time_spans"
    ensure(span, is_time_span)
    ensure(spans, is_time_spans)
    seq = []
    if not spans[1]:
        seq.append(span)
    else:
        for elem in strip_tag(spans):
            if precedes(start_time(span),start_time(elem)):
                seq.append(span)
                seq.append(strip_tag(spans)[strip_tag(spans).index(elem):][0])
            else:
                seq.append(elem)
                if not strip_tag(spans)[strip_tag(spans).index(elem)+1:]:
                    seq.append(span)
    return attach_tag('time_spans', seq)

def first_time_span(spans):
    "spans -> span"
    ensure(spans, is_time_spans)
    if is_empty_time_spans(spans):
        raise Exception('Empty spans.')
    else:
        return strip_tag(spans)[0]

def rest_time_spans(spans):
    "spans -> spans"
    ensure(spans, is_time_spans)
    if is_empty_time_spans(spans):
        return spans
    else:
        return attach_tag('time_spans', strip_tag(spans)[1:])

def for_each_span(spans, span_fn):
    "spans x (span ->) ->"
    if not is_empty_time_spans(spans):
        span_fn(first_time_span(spans))
        for_each_span(rest_time_spans(spans),span_fn)

def show_spans(spans):
    "spans ->"

    def show_spans_internal(ts):
        show_span(ts)
        print()

    for_each_span(spans,show_spans_internal)
