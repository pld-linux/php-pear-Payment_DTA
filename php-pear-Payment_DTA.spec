%include	/usr/lib/rpm/macros.php
%define         _class          Payment
%define         _subclass       DTA
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - creates DTA files containing money transactions (Germany)
Summary(pl):	%{_pearname} - tworzenie plików DTA zawieraj±cych transfery pieniê¿ne (Niemcy)
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d95badb708924107f5cda9decb24f888
URL:		http://pear.php.net/package/Payment_DTA/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} provides function to create DTA files used in Germany to
exchange information about money transactions with banks or online
banking programs.

This class has in PEAR status: %{_status}.

%description -l pl
%{_pearname} dostarcza funkcji do tworzenia plików DTA u¿ywanych w
Niemczech do wymiany informacji dotycz±cych transakcji pieniê¿nych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs
%{php_pear_dir}/%{_class}/*.php
