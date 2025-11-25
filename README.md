# Python Training – Exercises Repository

This repository is used to store all the code written during the **Python training** for the technical team.  
Each participant will push their solutions in dedicated branches: **one branch per exercise and per person**.

We expect only a small number of exercises, so the goal is to keep things simple and easy to navigate.

---

## Repository Purpose

- Centralize all training exercises in one place.
- Keep each participant’s work clearly separated via branches.
- Make it easy to review and compare different solutions for the same exercise.

The default branch will contain the baseline structure of the repository.  
**No one should commit directly to the default branch.**

---

## Exercises

The exercise specifications are available in the [`docs/`](./docs/) directory:

- **[Exercise 1 - Mini HR Manager](./docs/exercise1-hr-api.md)**: Build a Flask backend API to manage companies, roles, users, and employees.

---

## Branch Naming Convention

Each branch must follow this pattern:

```text
exercise-<number>/<firstname>
```

- `exercise-<number>`: the exercise number, written in lowercase and without spaces
  examples: exercise-1, exercise-2, exercise-3
- `<firstname>`: your first name, in lowercase
  examples: alice, benjamin, carla

### Examples

- `exercise-1/nicolas`
- `exercise-1/stewen`
- `exercise-2/nicolas`
- `exercise-3/stewen`

## Recommended Workflow

1. Update your local main branch
`git checkout main`
`git pull origin main`

2. Create a branch for your exercise

Example: exercise 1, by Nicolas:

`git checkout -b exercise-1/nicolas`

3. Implement your solution

Structure your code as you like within your branch. Remember everything is possible in Python. 🦄🌈

4. Commit your changes

Please use Conventional Commits for commit messages (e.g. feat:, fix:, docs:, etc.).

`git add .`
`git commit -m "feat: add solution for exercise 1"`

5. Push the branch to the remote repository

`git push -u origin exercise-1/nicolas`

7. (Optional) Open a Pull/Merge Request

Depending on how the trainer/team wants to proceed:
- Open a PR/MR from your branch to main (or another review branch).
- The trainer can then review, comment, and approve the solution.

---

## Project Structure

The baseline Flask app is organized by domain to keep responsibilities clear:

- `app/__init__.py` – Flask application factory, blueprint registration, error handlers
- `app/routes/` – HTTP routes grouped in Blueprints (e.g. `users.py`)
- `app/services/` – Domain logic orchestrating repositories and models
- `app/repositories/` – Data access code (SQLite users table)
- `app/models/` – Pydantic models shared across layers
- `users.sqlite3` – Local SQLite database seeded at startup

To start the API locally:

```
make install   # first time only
make run
```
