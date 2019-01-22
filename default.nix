with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    jupyter
    python36Packages.pandas
    python36Packages.requests
    python36Packages.matplotlib
    python36Packages.beautifulsoup4
  ];
}
