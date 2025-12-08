# polars-runtime-32-ft

This is a small package that provides Python 3.14t wheels specifically for the `polars` library. It is only compatible with *Polars 1.36.0b2*.

There are currently 2 wheels available:

- manylinux x86_64
- manylinux aarch64

## Installation

This is not available on PyPI. If you want to use polars free threaded in your project, I recommend to use `uv` with this in your pyproject.toml:

```toml
[project]
dependencies = [
    "polars==1.36.0b2",
    "polars-runtime-32"
]

[tool.uv.sources]
polars-runtime-32 = [
{ url = "https://github.com/harshil21/polars-runtime-32-ft/raw/refs/heads/main/wheels/polars_runtime_32-1.36.0b2-cp314-cp314t-manylinux_2_31_aarch64.whl", marker = "platform_machine == 'x86_64'" },
{ url = "https://github.com/harshil21/polars-runtime-32-ft/raw/refs/heads/main/wheels/polars_runtime_32-1.36.0b2-cp314-cp314t-manylinux_2_39_x86_64.whl", marker = "platform_machine == 'aarch64'" }
]

```

Then doing a regular `uv sync` should install the correct wheel for your platform.

## How it works

I compiled polars from source by editing the [Makefile](https://github.com/pola-rs/polars/blob/py-1.36.0-beta.2/Makefile) to add a new target for `cp314t` (Python 3.14t).

Specifically, I replaced the `maturin develop` with `maturin build`, and added the `--compatibility pypi` and `--target ... --zig` flags.
You also have to make sure that `ziglang` is pip installed in that script.

## Support

If you encounter any issues or have questions regarding this package, please open an issue.

This repository will be archived when polars officially supports Python 3.14t (i.e. with wheels).
See this PR for tracking: https://github.com/pola-rs/polars/pull/21914


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


