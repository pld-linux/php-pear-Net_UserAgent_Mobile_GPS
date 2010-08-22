%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	UserAgent_Mobile_GPS
%define		_status		alpha
%define		_pearname	Net_UserAgent_Mobile_GPS
Summary:	%{_pearname} - Interface for GPS
Summary(pl.UTF-8):	%{_pearname} - interfejs do GPS
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8f4f99c4defb7b3c0d5f5158b57879f2
URL:		http://pear.php.net/package/Net_UserAgent_Mobile_GPS/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_UserAgent_Mobile >= 0.1
Requires:	php-pear-PEAR-core >= 1:1.3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides methods to get GPS link for mobile device and to
parse GPS information.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten udostępnia sposoby na odczytanie informacji GPS z
urządzenia mobilnego.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/UserAgent/Mobile/GPS
%{php_pear_dir}/Net/UserAgent/Mobile/GPS.php
