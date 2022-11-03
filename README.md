# File Launcher

## This is an EXAMPLE script written in Python showing how to create a simple menu on the command line that lets you open a file with its default application

What this script do is the following:

1. Get all the files (not folders) in a directory.
2. Generate a list of their file names.
3. Return a numbered version of this list to the terminal.
4. Ask the number of the file to open.
5. Open the selected file with its default app.

## Requirements

This script was tested on *python 3.10.6* and use mainly native modules. The
only external module required is *pandas*. You can install it with *pip*:

```
pip install pandas
```

> If you don't have *pip*, install it with your package manager. For
ubuntu-based distibutions that could be:
>
> ```
> apt install python-pip
> ```

## How to use this example Python script in Linux

The easiest way to run this script for a non-technical user is to copy-paste or
download the file *launcher.py* to your computer.

> Another way to get the file from the terminal is using *wget*:
>
> ```
> wget http://github.com/USER_NAME/REPO_NAME/blob/COMMIT_ID/launcher.py
> ```

Then, you have to make it executable:

```
chmod -v +x file-launcher.py
```

Finnally, you can run it:

```
python3 file-launcher.py
```

> On some systems, *python* may still refer to Python 2 instead of Python 3.
I suggest the python3 binary to avoid ambiguity. If you still preffer call
*python* for brevity, you can create a link to it with the following command:
>
> ```
> sudo ln -s /usr/bin/python3 /usr/bin/python
> ```

By default it list files on the current user's *HOME* folder. To open another
folder, use the *-d* option (or the long option *--directory*):

```
python3 file-launcher.py -d /home/user/Documents
```

You can use environment variables too:

```
python3 file-launcher.py --directory $HOME/Images
```

## How to use this example Python script using Git

Comming soon
