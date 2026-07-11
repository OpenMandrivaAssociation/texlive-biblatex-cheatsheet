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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A BibLaTeX/Biber 'cheat sheet' which I wrote because I wanted one to
distribute to students, but couldn't find an existing one.

