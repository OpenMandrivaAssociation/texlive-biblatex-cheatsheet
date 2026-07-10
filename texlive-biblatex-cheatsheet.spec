%global tl_name biblatex-cheatsheet
%global tl_revision 44685

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	BibLaTeX/Biber cheat sheet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/biblatex-cheatsheet
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-cheatsheet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-cheatsheet.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A BibLaTeX/Biber 'cheat sheet' which I wrote because I wanted one to
distribute to students, but couldn't find an existing one.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-cheatsheet
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cheatsheet/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cheatsheet/biblatex-cheatsheet.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cheatsheet/biblatex-cheatsheet.tex
