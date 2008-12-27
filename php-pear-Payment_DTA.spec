%include	/usr/lib/rpm/macros.php
%define		_class		Payment
%define		_subclass	DTA
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - creates DTA files containing money transactions (Germany)
Summary(pl.UTF-8):	%{_pearname} - tworzenie plików DTA zawierających transfery pieniężne (Niemcy)
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	db34fa2c4ee017b8e579c7ab9b09bf66
URL:		http://pear.php.net/package/Payment_DTA/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear > 4:1.0-9.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} provides function to create DTA files used in Germany to
exchange information about money transactions with banks or online
banking programs.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
%{_pearname} dostarcza funkcji do tworzenia plików DTA używanych w
Niemczech do wymiany informacji dotyczących transakcji pieniężnych.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
