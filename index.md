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
blog on the Internet.[^ablog]

## Site contents

The main contents of this site are a blog that is intended to provide the
curious with a step by step guide to building their own bare metal
{term}`Kubernetes` cluster on their own hardware for less than the cost of
a single month of a managed cluster with a similar level of resources.

### Blog

```{toctree}

posts/index
```

### CI/CD Documentation

```{toctree}
:maxdepth: 3

.github/index
changelog
```

### Readme

```{toctree}
:maxdepth: 3

readme
```

## Metadata

Below are links to related repositories along with a glossary and perhaps
some links to indexes.

### Related repositories

- [ansible-etcd](https://edwardtheharris.github.io/ansible-etcd/)
- [ansible-kcp](https://edwardtheharris.github.io/ansible-kcp/)
- [ansible-k8s-nodes](https://edwardtheharris.github.io/ansible-k8s-nodes/)

### Glossary

```{glossary}
:sorted:

Ansible
  [Ansible](https://docs.ansible.com/) offers open-source automation
  that is simple, flexible, and powerful.

ArchLinux
  [ArchLinux](https://archlinux.org) is lightweight and flexible Linux®
  distribution that tries to Keep It Simple.

AWS
  [AWS](https://aws.amazon.com/) is a formerly innovative and useful collection
  of services that provides most of the revenue from which the Bezos' fortune
  is created. Like all monopolies or near monopolies it has become far too
  expensive for far little value. Don't use this.

Azure
  [Azure](https://azure.microsoft.com/en-us) seems to have become the latest
  method for MS to demand (DEMAND!) that you use Copilot. You shouldn't use
  Copilot, it will make you dumb and decrease your capacity for genuine
  understanding of even basic ideas like object permanence.

ECS
  [ECS](https://aws.amazon.com/ecs/?nc2=type_a) is kind of a first-draft
  version of Kubernetes, which is to say (even ten years on): half baked,
  feature-incomplete, too expensive, and for all but the simplest use cases
  almost entirely devoid of utility.

EKS
  [EKS](https://aws.amazon.com/eks/?nc2=type_a) is the admission by {term}`AWS`
  that {term}`ECS` was a total failure and they lost the betamax/vhs style
  brand war to Google's Kubernetes team. It's implementation is poor, Amazon
  seems to be insisting that you run the important parts of it on your own
  infrastructure, and has so little understanding of Kubernetes as a managed
  service that they can't even provide a believable estimate for the monthly
  cost of a cluster. Also don't use this.

etcd
  [etcd](https://etcd.io) is a strongly consistent, distributed key-value
  store that provides a reliable way to store data that needs to be accessed
  by a distributed system or cluster of machines. It gracefully handles leader
  elections during network partitions and can tolerate machine failure, even
  in the leader node.

git-cliff
  [git-cliff](https://git-cliff.org/) is a highly customizable
  changelog generator.

kubeadm
  [kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/) is a
  tool built to provide kubeadm init and kubeadm join as best-practice
  "fast paths" for creating Kubernetes clusters.

kubelet
  [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
  is the primary "node agent" that runs on each node. It can register
  the node with the apiserver using one of: the hostname; a flag to
  override the hostname; or specific logic for a cloud provider.

Kubernetes
  Kubernetes, also known as K8s, is an open source system for automating
  deployment, scaling, and management of containerized applications. Extensive
  use of the [related documentation](https://kubernetes.io/docs/home/) was
  made in the creation of this guide.

ssh
  [ssh](https://www.openssh.com/manual.html) is a basic rlogin/rsh-like
  client program

sudo
  [sudo](https://www.sudo.ws/) allows a system administrator to delegate
  authority to give certain users (or groups of users) the ability to run
  some (or all) commands as root or another user while providing an audit
  trail of the commands and their arguments.

  ... [okay, sudo make me a sandwich](https://xkcd.com/149/).

makepkg
  [makepkg](https://wiki.archlinux.org/title/Makepkg) is a script to automate
  the building of packages. The requirements for using the script
  are a build-capable Unix platform and a PKGBUILD.

yay
  Yet another Yogurt - An AUR Helper written in Go. See the related
  [GitHub Repository](https://github.com/Jguer/yay)
```

[^ablog]: This blog is generated using
  [ablog](https://ablog.readthedocs.io/en/stable/). The creators of
  ablog have no stated opinion on matters related to computing and
  its relationship with masochism.

<!-- vim: set colorcolumn=80: -->
