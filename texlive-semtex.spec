Name:		texlive-semtex
Version:	56530
Release:	1
Summary:	Deals with stripped SemanTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semtex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semtex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semtex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a small LaTeX package that adds a collection of
simple macros for parentheses and bullets. It exists for one
purpose only: To be loaded by documents which were originally
typeset using the package SemanTeX, but which have been
stripped of SemanTeX markup using the package stripsemantex
which is part of SemanTeX. Therefore, unless your document is
one of those, simply don't use this package. And even if your
document is one of those, there is a good chance you will not
have to load it after all. In most cases, you will be able to
replace the macros it provides by macros from other packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/semtex
%doc %{_texmfdistdir}/doc/latex/semtex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
