#include <string>
#include <vector>
#include <memory>
#include <cmath>
#include <iostream>


class facility_t {
public:
  double fx, fy;
  std::string fname;
  facility_t operator-(const facility_t f) {
      return {fx-f.fx,fy-f.fy,fname};
  };
};

class client_t {
public:
  double cx, cy;
  std::string cname;
  client_t operator-(const client_t c) {
      return {cx-c.cx,cy-c.cy,cname};
  };
};

class solution_t {
public:
  virtual double goal() const = 0;
};

class tsp_solution_t : public solution_t {
public:

  double goal() const {
      double distance_sum = 0.0;

      return distance_sum;
  }
};

int main() {
    using namespace std;


    return 0;
}
