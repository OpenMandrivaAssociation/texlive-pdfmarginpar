Name:		texlive-pdfmarginpar
Version:	23492
Release:	1
Summary:	Generate marginpar-equivalent PDF annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfmarginpar
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmarginpar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmarginpar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the \pdfmarginpar command which is similar
in spirit to \marginpar. However, it creates PDF annotations
which may be viewed with Adobe Reader in place of marginal
texts. Small icons indicate the in-text position where the
message originates, popups provide the messages themselves.
Thus bugfixes and other such communications are clearly visible
together when viewing the document, while the document itself
is not obscured.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfmarginpar/pdfmarginpar.sty
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/README
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginpar.pdf
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginpar.tex
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginparexample.pdf
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginparexample.png
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginparexample.tex
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/pgfmanual-en-macros.tex
%doc %{_texmfdistdir}/doc/latex/pdfmarginpar/pgfplots-macros.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
