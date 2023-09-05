# Bittensor Charter
***
This repository contains the Bittensor Charter, as developed by the Opentensor Foundation. This also contains a list of signatures from official entities that support the charter and the Bittensor project.

### Update signatures.json process
Note: This is a separate repository from bittensor and you must execute the scripts from here
(that is, *not* from the bittensor repository.)

For general guidance on how to clone and submit your changes see Github's official documentation:

* [How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
* [How to submit a PR from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

### Signature Instructions
***

1. From this repository, execute sign_charter.py and follow the prompts:
```
$ python sign_charter.py
Your validator's descriptive name (e.g. Opentensor Foundation):
Openτensor Foundaτion

Your validator url (e.g. www.opentensor.org ) [Optional]:
https://www.opentensor.ai/

The mnemonic of your validator's hotkey ( default location: ~/.bittensor/wallets/<coldkey>/hotkeys/<validator> )
das ist mir wurst
```

1. This will automatically update `signatures.json` with your information. You may then 
open a PR with your changes:
    1. An example of an [opened PR](https://github.com/opentensor/bittensor-charter/pull/1) .
1. If all of the checks pass, you may request a review and your delegates will be added to the list.
