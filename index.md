---
abstract: >-
  Kubernetes for Contrarian Fools documentation master file, created by
  sphinx-quickstart on Mon Jun 23 11:06:08 2025.
  You can adapt this file completely to your liking, but it should at least
  contain the root `toctree` directive.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-06-23
title: Kubernetes for Contrarian Fools documentation
---

Welcome to {term}`Kubernetes` for Contrarian Fools, the most masochistic
blog on the Internet.[^ablog]

## Site contents

The main contents of this site are a blog that is intended to provide the
curious with a step by step guide to building their own bare metal
{term}`Kubernetes` cluster on their own hardware for less than the cost of
a single month of a managed cluster with a similar level of resources.

### Blog

```{toctree}
:caption: posts

posts/index
```

### CI/CD Documentation

```{toctree}
:caption: integration and delivery
:maxdepth: 3

.github/index
changelog
```

## Metadata

Below are links to related repositories along with a glossary and perhaps
some links to indexes.

```{toctree}
:caption: meta
:maxdepth: 3

glossary
readme
```

### Related repositories

- [ansible-etcd](https://edwardtheharris.github.io/ansible-etcd/)
- [ansible-kcp](https://edwardtheharris.github.io/ansible-kcp/)
- [ansible-k8s-nodes](https://edwardtheharris.github.io/ansible-k8s-nodes/)

[^ablog]:
    This blog is generated using
    [ablog](https://ablog.readthedocs.io/en/stable/). The creators of
    ablog have no stated opinion on matters related to computing and
    its relationship with masochism.

<!-- vim: set colorcolumn=80: -->
