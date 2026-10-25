# Heating Management

A custom [Home Assistant](https://www.home-assistant.io/) integration for managing heating.

> **Status:** early development. The integration currently contains the example
> platforms (sensor, binary sensor, switch) and API client from
> [ludeeus/integration_blueprint](https://github.com/ludeeus/integration_blueprint),
> renamed to `heating_management`. They will be replaced by the real heating logic.

## Installation

### HACS (custom repository)

1. In HACS, open the menu (⋮) → **Custom repositories**.
1. Add `https://github.com/Meraxa/home-assistant-heating-management` with category **Integration**.
1. Install **Heating Management** and restart Home Assistant.

### Manual

1. Copy `custom_components/heating_management` into the `custom_components` folder of your Home Assistant configuration.
1. Restart Home Assistant.

## Configuration

Go to **Settings → Devices & services → Add integration** and search for **Heating Management**.

## Development

The easiest way to develop is the included VS Code devcontainer:

1. Open the repository in VS Code and choose **Reopen in Container**.
1. Run `scripts/develop` to start a Home Assistant instance at <http://localhost:8123> with this integration loaded (config lives in [`config/`](config/configuration.yaml)).
1. Run `scripts/lint` to format and lint the code with Ruff.

### Workflow

`main` is only changed through pull requests — never commit or push to it directly.

1. Create a branch from `main` (e.g. `feature/<topic>` or `fix/<topic>`).
1. Commit your changes and push the branch.
1. Open a pull request against `main`; the **Lint** and **Validate** (hassfest + HACS) workflows must pass before merging.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Spec-driven development

Features are specified with [OpenSpec](https://openspec.dev/) before they are implemented.
Current specs live in [`openspec/specs/`](openspec/specs/), proposed changes in [`openspec/changes/`](openspec/changes/).

The workflows are tool-agnostic agent skills in [`.agents/skills/`](.agents/skills/), usable by any coding agent that supports the shared `.agents` skills directory:

1. `openspec-explore` — think through an idea (optional).
1. `openspec-propose` — create a change with a proposal, spec deltas, design and tasks.
1. `openspec-apply-change` — implement the tasks.
1. `openspec-archive-change` — merge the spec deltas into `openspec/specs/` and archive the change.

`openspec-sync-specs` and `openspec-update-change` cover syncing specs without archiving and revising a change's plan.

The skills need the OpenSpec CLI (`npm install -g @fission-ai/openspec`), which also offers `openspec list`, `openspec show <change>` and `openspec validate <change>`.
Project context for the workflows is set in [`openspec/config.yaml`](openspec/config.yaml).
To add tool-specific commands for a particular agent later, run `openspec init --tools <tool>`.

### Repository layout

File | Purpose
-- | --
`custom_components/heating_management/` | The integration itself.
`config/configuration.yaml` | Home Assistant config used by `scripts/develop`.
`scripts/` | `setup`, `develop` and `lint` helper scripts.
`openspec/` | OpenSpec specs and change proposals.
`.agents/skills/` | OpenSpec workflow skills for coding agents.
`.devcontainer.json` | VS Code devcontainer definition.
`.github/workflows/` | CI: Ruff lint/format check, hassfest and HACS validation.
`.github/renovate.json` | Dependency updates via Renovate (`.github/_dependabot.yml` is a disabled Dependabot alternative — keep only one).
`requirements_*.txt` | Python dependencies for development and linting.

## Credits

Based on [ludeeus/integration_blueprint](https://github.com/ludeeus/integration_blueprint) (MIT).
