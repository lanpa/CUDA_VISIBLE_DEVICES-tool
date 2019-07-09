# usegpu
A convenient script to switch visible Nvidia GPU.

# install
```bash
wget https://raw.githubusercontent.com/lanpa/usegpu/master/appendtobash && cat appendtobash>>~/.bashrc
source ~/.bashrc

```

# usage

```bash
usegpu 1       # use gpu 1
usegpu 1,2     #usegpu 1 and 2
usegpu 0,2     #usegpu 0 and 2
usegpu         #show current visible gpu
```
