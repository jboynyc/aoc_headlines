with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    jupyter
    python37Packages.pandas
    python37Packages.requests
    python37Packages.matplotlib
    python37Packages.beautifulsoup4
  ];
}
