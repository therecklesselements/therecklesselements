/*
 * AIARE owned fixture v1.0.0 (2026-11-11)
 * Copyright (c) THE RECKLESS ELEMENTS.
 * Original minimal program authored for permissioned REA/Codex smoke tests.
 * The investigator must receive ONLY the compiled executable, not this source.
 *
 * Expected outputs are kept in a separate independent verifier.
 */
#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

static int transform(int value) {
    if (value < 0) {
        return 3 - value;
    }
    if (value == 0) {
        return 11;
    }
    if (value % 2 == 0) {
        return value * 2 + 1;
    }
    return value * 3 - 2;
}

int main(int argc, char **argv) {
    char *end = NULL;
    long parsed;

    if (argc != 2) {
        fputs("usage: owned_transform <integer -100..100>\n", stderr);
        return 2;
    }

    errno = 0;
    parsed = strtol(argv[1], &end, 10);
    if (errno != 0 || end == argv[1] || *end != '\0'
        || parsed < -100 || parsed > 100
        || parsed < INT_MIN || parsed > INT_MAX) {
        fputs("invalid input\n", stderr);
        return 2;
    }

    printf("%d\n", transform((int)parsed));
    return 0;
}
