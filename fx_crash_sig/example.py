from __future__ import print_function

import ujson as json
from siggen.generator import SignatureGenerator

from fx_crash_sig import sample_traces
from fx_crash_sig.symbolicate import Symbolicator

if __name__ == '__main__':
    symbolicator = Symbolicator()

    trace_dict = json.loads(sample_traces.string_trace1)

    symbolicated = symbolicator.symbolicate(trace_dict)

    print(symbolicated)

    symbolicated_list = symbolicator.symbolicate_multi([
        sample_traces.trace1,
        sample_traces.trace2,
        sample_traces.trace3,
    ])

    sig_generator = SignatureGenerator()

    print(sig_generator.generate(symbolicated))

    signatures = [sig_generator.generate(sym) for sym in symbolicated_list]

    print([sig['signature'] for sig in signatures])

    pass