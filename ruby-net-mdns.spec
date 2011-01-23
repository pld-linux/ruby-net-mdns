%define tarname net-mdns
Summary:	DNS Service Discovery module for Ruby
Summary(pl.UTF-8):	Moduł DNS Service Discovery dla języka Ruby
Name:		ruby-net-mdns
Version:	0.3
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/8387/%{tarname}-%{version}.tgz
# Source0-md5:	741d836a64fb8c72aeb781335c3f9a85
URL:		http://dnssd.rubyforge.org/net-mdns/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.3.1
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DNS Service Discovery module for Ruby.

%description -l pl.UTF-8
Moduł DNS Service Discovery (wykrywania usługi DNS) dla języka Ruby.

%prep
%setup -q -n %{tarname}-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{ruby_rubylibdir}/*
