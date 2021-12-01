using System;
using System.IO;
using System.Linq;

namespace AOC_CS.Days
{
    class Day01
    {
        const string INPUT_FILE = "Inputs/day01.txt";

        private int[] inputs;

        public Day01()
        {
            this.inputs = null;
        }

        private void ReadInput()
        {
            if (this.inputs is not null) return;

            var lines = File.ReadAllLines(INPUT_FILE);
            this.inputs = lines.Select(x => int.Parse(x)).ToArray();
        }

        public int SolveGeneral(int window = 1)
        {
            if (window < 1)
                throw new ArgumentException($"Invalid value for \"window\", allowed values are positive integers, got {window}");

            this.ReadInput();

            var result = 0;
            for (var i = window; i < this.inputs.Length; ++i)
            {
                if (this.inputs[i] > this.inputs[i - window]) ++result;
            }
            return result;
        }

        public int Solve1()
        {
            return this.SolveGeneral();
        }

        public int Solve2()
        {
            return this.SolveGeneral(3);
        }
    }
}
