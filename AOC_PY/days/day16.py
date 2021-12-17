import os
from functools import reduce
from typing import Optional

INPUT_PATH = os.path.join(os.path.dirname(__file__), '../../Inputs', 'day16.txt')


class Package:
    def __init__(self, version: int, type_id: int, value=0):
        self.version = version
        self.type_id = type_id
        self.value = value
        self.sub_packages: list[Package] = []

    def add_package(self, package):
        self.sub_packages.append(package)

    def sum_versions(self):
        result = self.version
        for pkg in self.sub_packages:
            result += pkg.sum_versions()
        return result

    def compute_value(self):
        if self.type_id == 4:
            return self.value
        values = [pkg.compute_value() for pkg in self.sub_packages]
        if self.type_id == 0:
            return sum(values)
        elif self.type_id == 1:
            return reduce(lambda res, cur: res * cur, values, 1)
        elif self.type_id == 2:
            return min(values)
        elif self.type_id == 3:
            return max(values)
        elif self.type_id == 5:
            return 1 if values[0] > values[1] else 0
        elif self.type_id == 6:
            return 1 if values[0] < values[1] else 0
        elif self.type_id == 7:
            return 1 if values[0] == values[1] else 0
        return None


def parse_package_structure_impl(bin_str: str, pos: int):
    version = int(bin_str[pos:pos + 3], base=2)
    type_id = int(bin_str[pos + 3:pos + 6], base=2)
    if type_id == 4:  # literal value
        cur_pos = pos + 6
        value = ''
        while True:
            value += bin_str[cur_pos + 1:cur_pos + 5]
            is_final = bin_str[cur_pos] == '0'
            cur_pos += 5
            if is_final:
                break
        pkg = Package(version=version, type_id=type_id, value=int(value, base=2))
        return pkg, cur_pos - pos  # package version, package length
    # operator
    length_type_id = bin_str[pos + 6]
    if length_type_id == '0':  # next 15 bits = total length of sub-packets
        sub_length = int(bin_str[pos + 7:pos + 22], base=2)
        total_lengths = 0
        pkg = Package(version=version, type_id=type_id)
        while total_lengths < sub_length:
            sub_pkg, pkg_len = parse_package_structure_impl(bin_str, pos=pos + 22 + total_lengths)
            pkg.add_package(sub_pkg)
            total_lengths += pkg_len
        return pkg, 22 + total_lengths
    # next 11 bits = number of sub-packets
    sub_count = int(bin_str[pos + 7:pos + 18], base=2)
    total_lengths = 0
    pkg = Package(version=version, type_id=type_id)
    for i in range(sub_count):
        sub_pkg, pkg_len = parse_package_structure_impl(bin_str, pos=pos + 18 + total_lengths)
        pkg.add_package(sub_pkg)
        total_lengths += pkg_len
    return pkg, 18 + total_lengths


def parse_package_structure(hex_str: str):
    bits = format(int(hex_str, base=16), f'0>{4 * len(hex_str)}b')
    pkg, _ = parse_package_structure_impl(bits, pos=0)
    return pkg


class Day16:
    def __init__(self):
        with open(INPUT_PATH, 'r') as infile:
            self.inputs = infile.readline().strip()
            self.pkg: Optional[Package] = None

    def _parse_package(self):
        if self.pkg is not None:
            return
        self.pkg = parse_package_structure(self.inputs)

    def solve1(self):
        self._parse_package()
        return self.pkg.sum_versions()

    def solve2(self):
        self._parse_package()
        return self.pkg.compute_value()


def main():
    x = Day16()
    print(x.solve1())
    print(x.solve2())


if __name__ == '__main__':
    main()
