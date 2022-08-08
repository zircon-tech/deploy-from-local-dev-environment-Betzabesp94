from brownie import accounts, config, Voting, network


def deploy_smart_contract():
    deployer = get_account()
    voting_comntract = Voting.deploy(
        {"from": deployer}, publish_source=True
    )  # deploy and verify
    print(voting_comntract)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_smart_contract()
