%global tl_name semtex
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.45
Release:	%{tl_revision}.1
Summary:	Deals with stripped SemanTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/semtex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semtex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is a small LaTeX package that adds a collection of simple
macros for parentheses and bullets. It exists for one purpose only: To
be loaded by documents which were originally typeset using the package
SemanTeX, but which have been stripped of SemanTeX markup using the
package stripsemantex which is part of SemanTeX. Therefore, unless your
document is one of those, simply don't use this package. And even if
your document is one of those, there is a good chance you will not have
to load it after all. In most cases, you will be able to replace the
macros it provides by macros from other packages.

