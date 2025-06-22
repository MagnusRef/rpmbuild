Name:           sveltosctl
Version:        0.57.2
Release:        1%{?dist}
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
* Sun Jun 22 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.57.2
* Sat May 3 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.53.0
* Sun Apr 20 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.52.1
* Sun Apr 13 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.51.1
* Sat Mar 22 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.50.0
* Wed Feb 26 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.49.0
* Mon Feb 10 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to v0.47.0
* Fri Feb 07 2025 MagnusRC <magnusrc@protonmail.com>
- Initial package release

