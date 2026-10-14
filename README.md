# Assembly Native

8086/x86 assembly programs covering strings, numeric algorithms, matrices, DOS system services, and interactive graphics.

The programs are organized by function, with source files, screenshots, and build guidance for each component.

## Programs

| Area | Program | Concepts |
|---|---|---|
| Strings | [Palindrome checker](strings/palindrome) | Indexed traversal and comparisons |
| Strings | [Case-insensitive matching](strings/case-insensitive-matching) | Character normalization and matching |
| Numbers | [Perfect-number checker](numbers/perfect-number) | Division, factors, and accumulation |
| Numbers | [Prime and sequence operations](numbers/prime-and-sequences) | Branches, loops, and console output |
| Matrices | [Matrix multiplication](matrices/multiplication) | Nested loops and indexed memory |
| System | [Current time](system/current-time) | DOS interrupts and formatted output |
| Graphics | [Interactive checker board](graphics/checker-board) | Screen drawing and keyboard/mouse input |

Each program keeps its own README, source files, and available screenshots.

## Toolchain

The programs target 16-bit DOS and use Microsoft Macro Assembler syntax. A typical setup uses:

- DOSBox or DOSBox-X
- MASM with the `ml` command available inside the emulator

From a program's `src` directory:

```text
ml main.asm
main.exe
```

Generated `.OBJ` and `.EXE` files are intentionally excluded from version control. Exact inputs and expected output are documented in each program directory.

## Scope

These low-level implementations focus on register operations, memory access, DOS services, algorithms, and graphics without framework abstractions.

## Provenance

See [PROVENANCE.md](PROVENANCE.md) for source history and attribution.

## License

No repository-wide open-source license is declared. See the source history for component-level licensing details.
