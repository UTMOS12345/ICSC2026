# ICSC2026

> My Python solutions to problems from the ICSC 2026 programming competition.

This repo has my solutions to the ICSC 2026 problems, plus a PDF that explains the idea behind each solution. Every solution reads its input from standard input and prints the answer, the way the judge expects.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Solutions](#solutions)
- [Maintainers](#maintainers)
- [License](#license)

## Background

ICSC is a programming competition where each problem gives a fixed input and output format. The `# --- Main execution block. DO NOT MODIFY ---` part of each file comes from the official template; my code is the function above it.

`ICSC.pdf` walks through the solutions step by step, with the code and the reasoning.

## Install

### Dependencies

- Python 3.8+
- No third-party packages

```bash
git clone https://github.com/UTMOS12345/ICSC2026
cd ICSC2026
```

## Usage

Each solution reads from standard input. Type the input, or pipe it in:

```bash
# Shape generator: size, then shape name
printf "5\ndiamond\n" | python problem_b.py

# Fighting game: starting HP, number of events, then "player frame damage" per line
printf "100\n3\n1 0 30\n2 0 50\n1 2 80\n" | python problem_d.py
```

## Solutions

| File | Problem | Idea |
|---|---|---|
| `problem_b.py` | Problem B: draw a `checkerboard` or `diamond` on an N×N grid of 0s and 1s | Checkerboard: parity of `x + y`. Diamond: cells whose Manhattan distance from the centre is at most `N // 2`. |
| `problem_d.py` | Problem D: two players attack each other in frames; find both players' final HP | Group attacks by frame, apply frames in time order, and stop at the first frame where someone hits 0 HP, so attacks in the same frame still count. HP is clamped to 0. |
| `ICSC.pdf` | Write-up of the solutions | Step-by-step explanation |
| `main.py` | Empty placeholder | — |

## Maintainers

[@UTMOS12345](https://github.com/UTMOS12345)

## License

No license has been chosen yet. Until one is added, all rights are reserved © Imomaliyev Maksudali.
