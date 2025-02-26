Name:           sveltosctl
Version:        0.49.0
Release:        2%{?dist}
Summary:        Project Sveltos cmd line tool

License:        Apache-2.0
URL:            https://projectsveltos.github.io/sveltos/
Source0:        https://github.com/projectsveltos/sveltosctl/releases/tag/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: golang, git

%description
Project Sveltos commandline tool for managing Sveltos resources.

%prep
%setup -q

%build
cd cmd/%{name}
go build -v -o ../../%{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Wed Feb 26 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.49.0
* Tue Feb 18 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.48.0
* Mon Feb 10 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.47.0
* Fri Feb 07 2025 MagnusRC <magnusrc@protonmail.com>
- Initial package release

