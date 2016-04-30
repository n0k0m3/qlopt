#include <tsqr.h>

namespace thesis{
	tsqr::tsqr(const size_t n, const size_t p)
	{
		init(n, p);
	}
			
	void tsqr::init(const size_t n, const size_t p)
	{
		num_obs = n;
		order = p;
		w = gsl_multilarge_linear_alloc(gsl_multilarge_linear_tsqr, p);
		X    = gsl_matrix_alloc(num_obs, order);
		gslx = gsl_vector_alloc(num_obs);
		gsly = gsl_vector_alloc(num_obs);
		c    = gsl_vector_alloc(order);
		lambda = 0.0;
	}

	tsqr::~tsqr()
	{
		gsl_multilarge_linear_free(w);
		gsl_matrix_free(X);
		gsl_vector_free(gslx);
		gsl_vector_free(gsly);
		gsl_vector_free(c);
	}
	
	void tsqr::update(const vec& x, const vec& y)
	{
		vecToGslVec(x, gslx);
		vecToGslVec(y, gsly);
		generateX(X, gslx);
		gsl_multilarge_linear_reset(w);
		gsl_multilarge_linear_accumulate(X, gsly, w);
		gsl_multilarge_linear_solve (lambda, c, &rnorm, &snorm, w);
	}
	
	void tsqr::vecToGslVec(const vec& v, gsl_vector* gslv)
	{	
		for (size_t i=0; i<gslv->size; i++){
			gsl_vector_set(gslv, i, v(i));
		}
	}

	void tsqr::generateX(gsl_matrix *M, gsl_vector* gslv)
	{
		gsl_vector *temp = gsl_vector_alloc(order);
		for (size_t i=0; i<M->size1; i++){
			generate_xi(gsl_vector_get(gslv, i), temp);
			gsl_matrix_set_row(M, i, temp);
		}
	}
	
	void tsqr::generate_xi(double xi, gsl_vector *gslv)
	{
		for (size_t i=0; i<order; i++){
			gsl_vector_set(gslv, i, pow(xi,i));
		}
	}
	
	double tsqr::interpolate(double xi)
	{
		double y = gsl_vector_get(c,0);
		for(int i = 1; i<order; i++){	
			y += gsl_vector_get(c,i)*pow(xi,i);
		}
		return y;
	}
}