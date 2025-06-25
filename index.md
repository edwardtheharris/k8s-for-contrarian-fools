---
abstract: >-
  Kubernetes the Hard Way documentation master file, created by
  sphinx-quickstart on Mon Jun 23 11:06:08 2025.
  You can adapt this file completely to your liking, but it should at least
  contain the root `toctree` directive.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-06-23
title: Kubernetes the Hard Way documentation
---

Welcome to {term}`Kubernetes` the Hard Way, the most masochistic
blog on the Internet.

## Posts

```{toctree}
posts/index
```

## Extensions et cetera

This blog is generated using [ablog](https://ablog.readthedocs.io/en/stable/).

```{toctree}
.github/index
readme
```

### Glossary

```{glossary}
ArchLinux
  [ArchLinux](https://archlinux.org) is lightweight and flexible Linux®
  distribution that tries to Keep It Simple.

etcd
  [etcd](https://etcd.io) is a strongly consistent, distributed key-value
  store that provides a reliable way to store data that needs to be accessed
  by a distributed system or cluster of machines. It gracefully handles leader
  elections during network partitions and can tolerate machine failure, even
  in the leader node.

Kubernetes
  Kubernetes, also known as K8s, is an open source system for automating deployment,
  scaling, and management of containerized applications. Extensive use of
  the [related documentation](https://kubernetes.io/docs/home/) was made in the
  creation of this guide.

makepkg
  [makepkg](https://wiki.archlinux.org/title/Makepkg) is a script to automate
  the building of packages. The requirements for using the script
  are a build-capable Unix platform and a PKGBUILD.

yay
  Yet another Yogurt - An AUR Helper written in Go. See the related
  [GitHub Repository](https://github.com/Jguer/yay)
```

<!-- vim: set colorcolumn=80: -->
