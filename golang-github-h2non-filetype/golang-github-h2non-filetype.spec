# Generated by go2rpm 1
%bcond_without check

# https://github.com/h2non/filetype
%global goipath         github.com/h2non/filetype
Version:                1.0.12

%gometa

%global common_description %{expand:
Small, dependency-free, fast Go package to infer binary file types based on the
magic numbers signature.}

%global golicenses      LICENSE
%global godocs          History.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Small, dependency-free, fast Go package to infer binary file types based on the magic numbers signature

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Apr 09 17:59:25 +03 2020 ElXreno <elxreno@gmail.com> - 1.0.12-1
- Initial package

