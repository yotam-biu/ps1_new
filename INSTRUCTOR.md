# Instructor setup

This is a new student template based on yotam-biu/ps1, commit
f9a938722a999ca1798ccf18299d1fe0324449be. The original repository is unchanged.

## Publish the template

Create an empty GitHub repository named `ps1_new` under your account, without
adding a README or license. From this local folder run:

```bash
git add .
git commit -m "Prepare PS1 student template"
git remote add origin https://github.com/yotam-biu/ps1_new.git
git push -u origin main
```

Enable **Template repository** in its GitHub settings if Classroom 50 offers
template selection. Choose this repository when creating the assignment.
The precise Classroom 50 setup and numeric score ingestion have not been
verified in an authenticated classroom session. The workflow uses standard
GitHub Classroom command graders and the grading reporter (10 points total).

Before distributing the invitation, accept it using a test student account,
check that files and Actions are copied, submit a correct answer, and confirm
both the green workflow result and the displayed 10/10 in Classroom 50.
If only pass/fail is shown, inspect Classroom 50's supported grading settings.

## Changes from the original

- Retains the original four-line exercise and starter value.
- Clarifies that students supply spacing and punctuation through `name`.
- Replaces fragile raw-line matching with syntax-tree checks, allowing harmless
  formatting and quote changes while preserving the required statements.
- Runs two explicit, independent 5-point tests with feedback and time limits.
- Uses no pip dependencies and removes the redundant shell script.
- Adds Hebrew instructions and a notebook that points back to hello.py.
- Removes stale links to the original repository from the notebook.

These are visible practice tests. They are not tamper-proof grading: students
who can edit the repository can also modify its tests/workflow. For this small
introductory exercise, review hello.py when finalizing grades. Use an external
trusted grader if you need enforcement against deliberate test modifications.

## Local verification

```bash
python3 .tests/test_hello.py
```

The template should fail both tests. This is expected before a student edits it.
