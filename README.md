# Rule 110 hardware implementation

English | [Русский](README.ru.md)

Articles on Habr (in Russian): [1](https://habr.com/ru/articles/1105190), [2](https://habr.com/ru/articles/1105450/), [3]()

This project implements the Rule 110 cellular automaton using standard 4000-series CMOS logic ICs.

It processes cells sequentially, which dramatically reduces the number of ICs required.

![Board](images/board.jpg)

The sequential nature of this solution requires a sequential output device; here, the evolution of the cellular automaton is displayed on an analog oscilloscope.

![110 triangle on scope](images/triangle_on_scope.jpg)

Licensed under the MIT License. Applies to all files in this repository, including schematics, documentation, scripts and images.
