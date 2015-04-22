**pybbbcli - Python Bicycle Blue book CLI client**

**What is this pybbbcli?**

As a geek and cycling team we often end up checking information on **http://www.bicyclebluebook.com/** and
since we have some spare time on our hands we decided to give it a try and build a light CLI client
that we can run from a terminal.

**How to i use it?**

clone the repository and do:

* pip install -r requirements.txt

on your client build the logic needed:

    from pybbbcli import Pybbbcli

    bbb = Pybbbcli()

    bbb.search("make")
    bbb.showBrands()
    bbb.select("make")

This is still work in progress.
