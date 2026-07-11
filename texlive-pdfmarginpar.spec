%global tl_name pdfmarginpar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.92
Release:	%{tl_revision}.1
Summary:	Generate marginpar-equivalent PDF annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfmarginpar
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmarginpar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmarginpar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the \pdfmarginpar command which is similar in
spirit to \marginpar. However, it creates PDF annotations which may be
viewed with Adobe Reader in place of marginal texts. Small icons
indicate the in-text position where the message originates, popups
provide the messages themselves. Thus bugfixes and other such
communications are clearly visible together when viewing the document,
while the document itself is not obscured.

