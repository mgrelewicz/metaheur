#include <string>
#include <vector>
#include <memory>
#include <cmath>
#include <iostream>


class facility_t {
public:
  double x, y;
  std::string name;
  facility_t operator-(const facility_t c) {
      return {x-c.x,y-c.y,name};
  };
  double len() {
      return std::sqrt(x*x+y*y);
  }
};
using problem_t = std::vector<city_t>;


class solution_t {
public:
  virtual double goal() const = 0;
};

class tsp_solution_t : public solution_t {
public:
  std::shared_ptr<problem_t> problem;
  std::vector<int> facilities_to_locate;
  double goal() const {
      double distance = 0.0;
      auto p = problem->at(facilities_to_locate.at(0));
      for (int i = 1; i <= problem->size(); i++) {
          distance += (p - problem->at(facilities_to_locate[i%problem->size()])).len();
          p = problem->at(facilities_to_locate[i%problem->size()]);
      }
      return distance;
  }
};

int main() {
    using namespace std;
    problem_t problem = {
        {1.0,1.0, "Lębork"},
        {5.0,1.0, "Kościerzyna"},
        {2.0,10.5, "Piekło Dolne"},
        {20.0,10.0, "Złe Mięso"}
    };

    tsp_solution_t sol;
    sol.problem = make_shared<problem_t>(problem);
    sol.facilities_to_locate = {0,1,2,3};
    cout << sol.goal() << endl;
    sol.facilities_to_locate = {1,2,0,3};
    cout << sol.goal() << endl;
    return 0;
}
