Name:           k9s
Version:        0.50.6
Release:        1%{?dist}
Summary:        Kubernetes CLI To Manage Your Clusters In Style!

License:        Apache-2.0
URL:            https://github.com/derailed/k9s
Source0:        https://github.com/derailed/k9s/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires:  golang git

%description
K9s provides a terminal UI to interact with your Kubernetes clusters.
The aim of this project is to make it easier to navigate,
observe and manage your applications in the wild.
K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%prep
%setup -q

%build
go build -v -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Sat May 17 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to version v0.50.6
* Fri May 9 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to version v0.50.5
* Sun Apr 20 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to version v0.50.4
* Sat Apr 12 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to version v0.50.2
* Tue Feb 18 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to version v0.40.5
* Sun Feb 16 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to version v0.40.0
* Sat Feb 08 2025 MagnusRC <magnusrc@protonmail.com>
- initial package release
