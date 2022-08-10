## Unit 3: Ethereum | Local Development Environments -English Version- 🚀

### Local Enviroment | Brownie

#### About Brownie

- Python-Based
- Build on Web3.py
- Pre-Configured Networks (Eth with Infura)
- Full support Solidity and Vyper

#### Requirements and Setup

Requirements:

- python3 version 3.6 or greater, python3-dev
- ganache-cli - tested with version 6.12.2

Setting up the local enviroment as describe on github [eth-brownie/brownie](https://github.com/eth-brownie/brownie), to see the Official Brownie Documentation [Eth-Brownie Docs](https://eth-brownie.readthedocs.io/en/latest/)

If you don't have Ganache, Run:

```
npm install ganache --global
```

Using PIPX (Recomended)

```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

```
python3 -m pip install --user pipx
```

```
pipx install eth-brownie
```

It might be python instead of python3 depending on your configuration

If you have problems you might want to check [pipx documentation](https://pypa.github.io/pipx/)

Quick Start

```
brownie init
```

Note: It must be initalized in an empty folder.

### ./contracts

Using the previos contract developed [Voting.sol](https://github.com/zircon-tech/smart-contract-using-remix-Betzabesp94/blob/main/Voting.sol)

### ./scripts

Writing a [deployment script ](https://eth-brownie.readthedocs.io/en/latest/deploy.html)

### brownie-config.yaml

Configuration file for the project

### .env (changing example.env)

You will need to set:

- PRIVATE_KEY (account of deployer)
- WEB3_INFURA_PROJECT_ID (Provider) if you want to see all the networks already configured then run:

```
brownie networks list
```

- ETHERSCAN_TOKEN (If you want to verify the smart contract)

Smart contract deployed on kovan testnet at: [0x947D0f6E593e30e0eE27f8D4BB6d4805fd1964e6](https://kovan.etherscan.io/address/0x947D0f6E593e30e0eE27f8D4BB6d4805fd1964e6)
