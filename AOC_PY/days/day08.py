import os
from typing import Iterable

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day08.txt')


def sorted_signal(signal: Iterable):
    return ''.join(sorted(signal))


def create_signal_decoder(patterns: tuple[str, ...]):
    pattern_sets = tuple(set(_) for _ in patterns)
    signal_encoder, signal_decoder = dict(), dict()

    # determine digits 1, 4, 7 and 8
    for pattern, pattern_set in zip(patterns, pattern_sets):
        if len(pattern_set) == 2:  # digit 1
            signal_encoder[1] = pattern_set
            signal_decoder[pattern] = 1
        elif len(pattern_set) == 3:  # digit 7
            signal_encoder[7] = pattern_set
            signal_decoder[pattern] = 7
        elif len(pattern_set) == 4:  # digit 4
            signal_encoder[4] = pattern_set
            signal_decoder[pattern] = 4
        elif len(pattern_set) == 7:  # digit 8
            signal_encoder[8] = pattern_set
            signal_decoder[pattern] = 8

    segment_encoder = {'a': signal_encoder[7].difference(signal_encoder[1])}
    p_bd = signal_encoder[4].difference(signal_encoder[1])
    p_cf = signal_encoder[1]
    p_eg = signal_encoder[8].difference(signal_encoder[4].union(signal_encoder[7]))

    # determine digits 0, 6 and 9
    for pattern, pattern_set in zip(patterns, pattern_sets):
        if len(pattern_set) != 6:
            continue
        diff_for_0 = pattern_set.difference(segment_encoder['a'].union(p_cf).union(p_eg))
        if len(diff_for_0) == 1:
            signal_decoder[pattern] = 0
            segment_encoder['b'] = diff_for_0
            segment_encoder['d'] = p_bd.difference(diff_for_0)
            continue
        diff_for_6 = pattern_set.difference(segment_encoder['a'].union(p_bd).union(p_eg))
        if len(diff_for_6) == 1:
            signal_decoder[pattern] = 6
            segment_encoder['f'] = diff_for_6
            segment_encoder['c'] = p_cf.difference(diff_for_6)
            continue
        diff_for_9 = pattern_set.difference(segment_encoder['a'].union(p_bd).union(p_cf))
        if len(diff_for_9) == 1:
            signal_decoder[pattern] = 9
            segment_encoder['g'] = diff_for_9
            segment_encoder['e'] = p_eg.difference(diff_for_9)

    # determine remaining digits (2, 3 and 5)
    signal_decoder[sorted_signal(segment_encoder['a'].union(segment_encoder['c'], segment_encoder['d'], p_eg))] = 2
    signal_decoder[sorted_signal(segment_encoder['a'].union(segment_encoder['d'], segment_encoder['g'], p_cf))] = 3
    signal_decoder[sorted_signal(segment_encoder['a'].union(segment_encoder['f'], segment_encoder['g'], p_bd))] = 5

    return signal_decoder


class Day08:
    def __init__(self):
        self.inputs = []
        with open(INPUT_PATH) as infile:
            for line in infile:
                patterns, digit_output = line.rstrip().split(' | ')
                self.inputs.append((
                    tuple(sorted_signal(_) for _ in patterns.split(' ')),
                    tuple(sorted_signal(_) for _ in digit_output.split(' '))
                ))

    def solve1(self):
        result = 0
        for patterns, outputs in self.inputs:
            decoder = create_signal_decoder(patterns)
            result += sum(1 if decoder[signal] in (1, 4, 7, 8) else 0 for signal in outputs)
        return result

    def solve2(self):
        result = 0
        for patterns, outputs in self.inputs:
            decoder = create_signal_decoder(patterns)
            result += int(''.join([str(decoder[signal]) for signal in outputs]))
        return result


def main():
    x = Day08()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
