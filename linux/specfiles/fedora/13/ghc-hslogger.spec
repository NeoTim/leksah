%global pkg_name hslogger

%global common_summary Haskell %{pkg_name} library

%global common_description A logging framework for Haskell

%global ghc_pkg_deps ghc-mtl-devel,ghc-network-devel

%bcond_without shared

# debuginfo is not useful for ghc
%global debug_package %{nil}

Name:           ghc-%{pkg_name}
Version:        1.0.10
Release:        1%{?dist}
Summary:        %{common_summary}

Group:          System Environment/Libraries
License:        LGPL
URL:            http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha
BuildRequires:  ghc, ghc-rpm-macros >= 0.5.1
BuildRequires:  ghc-doc
BuildRequires:  ghc-prof
%{?ghc_pkg_deps:BuildRequires:  %{ghc_pkg_deps}, %(echo %{ghc_pkg_deps} | sed -e "s/\(ghc-[^, ]\+\)-devel/\1-doc,\1-prof/g")}

%description
%{common_description}
%if %{with shared}
This package provides the shared library.
%endif

%ghc_lib_package


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%cabal_configure --ghc -p
%cabal build
%cabal haddock


%install
%cabal_install
%cabal_pkg_conf

%ghc_gen_filelists


%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Tue May 25 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 1.0.10-1
- initial packaging for Fedora automatically generated by cabal2spec-0.21.3
