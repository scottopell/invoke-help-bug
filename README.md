# Invoke --help flag handling bug repro

Running `inv example.generate --help` displays:
```
$ inv example.generate --help
Generating --help with default image
```

This is incorrect, `--help` should be handled as a core flag.

Ref: https://github.com/pyinvoke/invoke/issues/205


