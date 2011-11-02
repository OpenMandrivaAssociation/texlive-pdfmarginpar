Name:		texlive-pdfmarginpar
Version:	0.92
Release:	1
Summary:	Generate marginpar-equivalent PDF annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfmarginpar
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmarginpar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfmarginpar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides the \pdfmarginpar command which is similar
in spirit to \marginpar. However, it creates PDF annotations
which may be viewed with Adobe Reader in place of marginal
texts. Small icons indicate the in-text position where the
message originates, popups provide the messages themselves.
Thus bugfixes and other such communications are clearly visible
together when viewing the document, while the document itself
is not obscured.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
