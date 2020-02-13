# Generated by rust2rpm-9-1.fc31
%bcond_with check
%global debug_package %{nil}

%global crate dbus

Name:           rust-%{crate}0.2
Version:        0.2.3
Release:        3%{?dist}
Summary:        Bindings to D-Bus, which is a bus commonly used on Linux for inter-process communication.

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/dbus
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)
%if %{with check}
BuildRequires:  (crate(tempdir/default) >= 0.3.0 with crate(tempdir/default) < 0.4.0)
%endif
BuildRequires:  dbus-devel

%global _description \
Bindings to D-Bus, which is a bus commonly used on Linux for inter-process\
communication.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       dbus-devel

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 15:26:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Initial package
