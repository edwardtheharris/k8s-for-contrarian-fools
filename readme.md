---
abstract: This is the readme for the Kubernetes the hard way blog.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-06-22
title: Kubernetes for Contrarnain Fools Introduction
---

This blog is an attempt to document the process of building a Kubernetes
cluster using commodity hardware and some basic automation. The reason
the author is embarking on this voyage of dubious value is that he
requires a cluster with which to keep his skills sharp and despite
a local network with some twenty or more servers that includes primary
and secondary bind name servers, there are no systems presently available
to the author for repurposing as nodes in a Kubernetes cluster.

## Why not minikube or kind

There are a couple of reasons for this. The first is that, while kind or
minikube may be fine tools for a beginner that just wants to get their
feet wet with Kubernetes, anyone with enough experience will be able to
tell you that simulating a cluster is a wildly different activity from
actually running a cluster. Since the author intends to demonstrate
and expand expertise in the operation of Kubernetes clusters in the
enterprise it follows that he'll need a proper cluster to operate on.

If you've read much of the Kubernetes reference manual, you may have noticed
that the use of cloud services is [encouraged](https://kubernetes.io/docs/setup/production-environment/#production-considerations).
The author certainly did when he first started thumbing through it back in 2018.
Being the sort of curious, pedantic, and contrarian sort of fellow
that reads the sound advice provided by the manual to just do it the easy way
as a challenge instead of advice the author built his first Kubernetes cluster
for contrarian fools in 2018.

The manual was correct its assertion that knowing how to build a cluster
isn't necessarily useful in a production environment since (as the author
now has the experience to verify) an engineer will almost never be working
with bare metal in the wild. You just have to take it on faith that whichever
provider you're making do with has configured things correctly on their end.
And, when you're being paid to make the software run, this is fine. After all,
the alternative is to introduce the possibility of having to visit an actual
data center back into your life, and who wants that?

Still, the author is a curious monkey and he has an almost uncontrollable desire
to know how things work, even if only to support some future act of pedantry.

And, because the Kubernetes API is a forever changing and immensely complicated
system, building bare metal clusters on his local network has become something
of a habit for the author.

## Also, money

So the author finds himself without the means to support the cost of a
modest
[GKE](https://cloud.google.com/products/calculator?dl=CjhDaVF5WkRRd1pEZGtZUzA1TWpreUxUUTVZVFF0WWpSaU5TMWtPVEl4T1RNNE5HVTBZVGtRQVE9PRAPGiRDMkMwRjlBOS1GMjNFLTQ2RTMtQjZDMS0zN0ZDMkJEMDQ4QjY)
or [EKS](https://calculator.aws/#/estimate?id=8a9dd9e17e7d31f7a717c6759ae6ab4eef2ed112)
cluster but the need for a cluster on which to experiment and study
while at the same time having managed to consume every single node
he'd used to build his last half dozen or so bare metal clusters for
other services that he's come to rely on. In the way that a hammer
will always want a nail, the author finds himself in need of some
additional nodes.

### GKE

```{figure} _static/img/readme/gke-estimate.png
:align: left

At least Google is honest about the cost of this modest cluster.

|GKE|||
|---|---|---|
|nodes|3||
|vCPU|4|per node|
|memory|16gb|per node|
|storage|256gb "balanced"|per node|
|cost|$596.35||
```

### AWS

```{figure} _static/img/readme/eks-estimate.png
:align: left

AWS can't even tell you how much you're going to pay for a similarly
modest cluster in any believable or precise way.

Rest assured, though, that for the same configuration provided by Google
the figure quoted here
would at least double if not triple for an EKS cluster. A good deal of that
cost would be wrapped up in the question marks in the table below, but
this estimate doesn't really provide a way to be certain. It can be taken
as the cost of a single EKS control plane node.

|EKS|||
|---|---|---|
|nodes|3|hybrid|
|vCPU|4|per node|
|memory|???|per node|
|storage|???|per node|
|cost|$248.20/mo|*not including nodes, ingress, egress, or other fees|
```

Yikes! That'll really bust the budget of a skilled but income-free
computer programmer with rent to pay, which brings us to the solution
that will be documented here.

## Bare Metal

{attribution=" A bumper sticker"}
> There is no such thing as the cloud, it's just someone else's computer.

Which brings us to the purpose of this little doc, how to build a
functional (if not scalable) Kubernetes cluster on your own network
for less than the cost of a single month's (roughly) equivalent
compute resources.

The cluster will have 4 nodes, 1 control plane and 3 workers.

The control plane will run on a Lenovo ThinkCentre M910q.

```{figure} _static/img/readme/control-plane-node.png
:align: left
:scale: 55%

At a bit more than 100 dollars, we're already saving versus the AWS
estimate for an EKS control plane by more than half.
```

The worker nodes will run on 3 Lenovo ThinkCentre M710qs.

```{figure} _static/img/readme/worker-node.png
:align: left
:scale: 55%

At less than a hundred dollars each, these will cost less than $300,
or slightly more than the cost of an EKS control plane per month.

|Bare Metal|||
|---|---|---|
|nodes|3|m710q|
|cpu cores|2|per node|
|memory|16gb|per node|
|storage|256gb|per node|
```

These are old systems, but they are cheap and for the purposes of
the author or anyone that wants to build a fully-functional Kubernetes
cluster without having to take out a second mortgage, they will do just
fine. They won't be expected to run any enterprise scale workloads so,
while the author has setup bare metal clusters with high availability
in the past, these will be using a single control plane.

The total cost of this cluster so far, including shipping and a box
of protein bars is $439.25.

And with that, we [may begin](/index.md).
