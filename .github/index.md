---
abstract: Basic information about the CI/CD processes in this repo.
authors: Xander Harris
date: 2024-02-19
title: GitHub Actions configuration
---

## Dependabot

Stay away from zero days with Dependabot.

```{autoyaml} .github/dependabot.yml

```

## Workflows

GitHub Actions provides a pretty complete CI/CD system and they'll let you
run a lot of pipelines for free.

### Documentation

Build and deploy the GitHub Pages docs.

```{autoyaml} .github/workflows/documentation.yml

```

The docs are linted with
[markdownlint](https://github.com/DavidAnson/markdownlint-cli2) before the
build.

### Metadata

Add metadata to related issues and pull requests.

```{autoyaml} .github/workflows/metadata.yml

```
