# x86 Assembly Lab

A curated collection of 8086/x86 assembly exercises covering strings, numeric algorithms, matrices, DOS system services, and simple graphics.

This repository consolidates my original learning projects into one navigable lab. The implementations remain close to their original form; the surrounding structure and documentation are being standardized for reproducibility.

## Collections

| Area | Exercise | Concepts |
|---|---|---|
| Strings | [Palindrome checker](strings/palindrome) | Indexed traversal and comparisons |
| Strings | [Case-insensitive matching](strings/case-insensitive-matching) | Character normalization and matching |
| Numbers | [Perfect-number checker](numbers/perfect-number) | Division, factors, and accumulation |
| Numbers | [Prime and sequence operations](numbers/prime-and-sequences) | Branches, loops, and console output |
| Matrices | [Matrix multiplication](matrices/multiplication) | Nested loops and indexed memory |
| System | [Current time](system/current-time) | DOS interrupts and formatted output |
| Graphics | [Interactive checker board](graphics/checker-board) | Screen drawing and keyboard/mouse input |

Each exercise keeps its own README, source files, and available screenshots.

## Toolchain

The programs target 16-bit DOS and use Microsoft Macro Assembler syntax. A typical setup uses:

- DOSBox or DOSBox-X
- MASM with the `ml` command available inside the emulator

From an exercise's `src` directory:

```text
ml main.asm
main.exe
```

Generated `.OBJ` and `.EXE` files are intentionally excluded from version control. Exact inputs and expected output are documented in each exercise directory.

## Scope

These are educational implementations created while learning low-level programming. They are presented to demonstrate progression and fundamentals, not as production libraries.

## Provenance

The exercises were migrated from their original standalone GitHub repositories. See [PROVENANCE.md](PROVENANCE.md) for the source mapping.

## License

No blanket open-source license is applied yet. The original projects did not declare a license, so reuse permissions are intentionally not broadened during consolidation.
