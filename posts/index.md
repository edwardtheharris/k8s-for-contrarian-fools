---
abstract: Kubernetes the Hard Way index and contents.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-06-23
title: Index and Contents
---

This blog (novella question mark?) will be divided into sections for the
sake of the author's sanity and capacity for completing this rather large
project in digestible chunks, exactly the opposite of the way he eats food.

## Sections

The sections here will reflect the stages of deploying (and learning about)
a bare metal {term}`Kubernetes` cluster or clusters to commodity hardware
that will be running {term}`ArchLinux`. Some of the posts may reference
the {term}`ArchLinux` wiki because of this, and not at all because the
author of this blog (short story question mark?) also has editor credits
on the most relevant {term}`ArchLinux` wiki pages.

### Preparation

While it requires more effort and is an additional service to manage,
deploying a separate {term}`etcd`.

```{toctree}
01-etcd/index
```

```{postlist}
:sort:
:category: Preparation
```

### Proof of Concept

```{toctree}
02-q-and-d-kubeadm/index
```

### Miscellaneous

```{toctree}
00-misc/index
```

```{postlist}
:sort:
:category: Quick and Dirty
```

### The Control Plane

### The Worker Nodes

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>
```
