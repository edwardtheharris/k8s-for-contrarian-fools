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
deploying a separate {term}`etcd` can lead to a more stable cluster.

```{toctree}
01-etcd/index
```

{term}`Kubernetes` is a complex set of services that require patience
and planning when building it by hand.

```{postlist}
:sort:
:category: Preparation
```

### Proof of Concept

Sometimes, though, you just want a cluster to be running, and that's
what {term}`kubeadm` was made for.

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

```{toctree}
03-control-plane/index
```

```{postlist}
:sort:
:category: Control Plane
```

### The Worker Nodes

```{toctree}
04-workers/index
```

```{postlist}
:sort:
:category: Worker Nodes
```

### Workloads

Finally, we do some actual work. That's right everything until now
has been preparing to work.

```{toctree}
05-workloads/index
```

```{postlist}
:sort:
:category: Workloads
```

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```

> Take care of your tools and they'll take care of you.
>
> -- Unknown
