import { Clock, FileText, IndianRupee, AlertCircle, Globe, Building2, CheckCircle, Info, Shield, ListOrdered } from 'lucide-react'

export default function ServiceCard({ service }) {
  const getCategoryBadge = (category) => {
    const colors = {
      'A': 'bg-green-100 text-green-800',
      'B': 'bg-blue-100 text-blue-800',
      'E-Pass': 'bg-purple-100 text-purple-800'
    }
    return colors[category] || 'bg-gray-100 text-gray-800'
  }

  return (
    <div className="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow p-6 border border-gray-100">
      {/* Header */}
      <div className="flex justify-between items-start mb-4">
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-2">
            <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getCategoryBadge(service.category)}`}>
              Category {service.category}
            </span>
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-gray-100 text-gray-700">
              #{service.priority_rank}
            </span>
          </div>
          <h3 className="text-xl font-bold text-gray-900 mb-1">{service.name.en}</h3>
          <p className="text-gray-600 text-sm">{service.name.te}</p>
        </div>
      </div>

      {/* Description */}
      <p className="text-gray-700 mb-4 leading-relaxed">{service.description_simple.en}</p>

      {/* Fee Breakdown Section - NEW */}
      {service.fee_breakdown && (
        <div className="bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg p-4 mb-4 border border-green-200">
          <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
            <IndianRupee className="w-4 h-4" />
            Fee Breakdown
          </h4>
          <div className="space-y-2">
            <div className="flex justify-between items-center text-sm">
              <span className="text-gray-700">Service Fee:</span>
              <span className="font-medium text-gray-900">₹{service.fee_breakdown.service_fee}</span>
            </div>
            <div className="flex justify-between items-center text-sm">
              <span className="text-gray-700">MeeSeva Charge:</span>
              <span className="font-medium text-gray-900">₹{service.fee_breakdown.meeseva_charge}</span>
            </div>
            <div className="border-t border-green-300 pt-2 mt-2">
              <div className="flex justify-between items-center">
                <span className="font-semibold text-gray-900">Total Fee:</span>
                <span className="font-bold text-xl text-telangana-primary">₹{service.fee_breakdown.total}</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Info Grid */}
      <div className="grid grid-cols-2 gap-4 mb-4">
        <div className="flex items-start gap-2">
          <Building2 className="w-5 h-5 text-gray-400 mt-0.5 flex-shrink-0" />
          <div>
            <p className="text-xs text-gray-500">Department</p>
            <p className="font-semibold text-gray-800">{service.department}</p>
          </div>
        </div>
        <div className="flex items-start gap-2">
          <Clock className="w-5 h-5 text-gray-400 mt-0.5 flex-shrink-0" />
          <div>
            <p className="text-xs text-gray-500">Processing Time</p>
            <p className="font-semibold text-gray-800">{service.processing_time}</p>
          </div>
        </div>
      </div>

      {/* Application Mode Clarity - ENHANCED */}
      <div className="bg-gradient-to-r from-blue-50 to-orange-50 rounded-lg p-4 mb-4">
        <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
          <Globe className="w-4 h-4" />
          Application Mode
        </h4>
        <div className="grid grid-cols-2 gap-3">
          {/* Online Submission */}
          <div className={`p-3 rounded-lg ${service.submission_modes.online.available ? 'bg-green-50 border-2 border-green-300' : 'bg-gray-50 border-2 border-gray-200'}`}>
            <p className="font-medium text-sm mb-1 flex items-center gap-1">
              {service.submission_modes.online.available ? (
                <>
                  <CheckCircle className="w-4 h-4 text-green-600" />
                  <span className="text-green-700">Available Online</span>
                </>
              ) : (
                <>
                  <span className="text-gray-500">❌ Not Available Online</span>
                </>
              )}
            </p>
            {service.submission_modes.online.available && (
              <p className="text-xs text-gray-600">Apply from home</p>
            )}
          </div>

          {/* MeeSeva Center */}
          <div className={`p-3 rounded-lg ${service.submission_modes.meeseva_center.available ? 'bg-green-50 border-2 border-green-300' : 'bg-gray-50 border-2 border-gray-200'}`}>
            <p className="font-medium text-sm mb-1 flex items-center gap-1">
              {service.submission_modes.meeseva_center.available ? (
                <>
                  <CheckCircle className="w-4 h-4 text-green-600" />
                  <span className="text-green-700">Available at MeeSeva</span>
                </>
              ) : (
                <>
                  <span className="text-gray-500">❌ Not at MeeSeva</span>
                </>
              )}
            </p>
            {service.submission_modes.meeseva_center.available && service.submission_modes.meeseva_center.requires_stamp && (
              <p className="text-xs text-orange-600 font-semibold">⚠️ ₹2 Court Stamp required</p>
            )}
          </div>
        </div>
      </div>

      {/* Revenue Service Alert */}
      {service.is_revenue && service.submission_modes.meeseva_center.requires_stamp && (
        <div className="bg-orange-50 border border-orange-200 rounded-lg p-3 mb-4 flex items-start gap-2">
          <AlertCircle className="w-5 h-5 text-orange-600 flex-shrink-0 mt-0.5" />
          <div>
            <p className="text-sm font-semibold text-orange-800">Revenue Service Notice</p>
            <p className="text-xs text-orange-700 mt-1">
              This is a Revenue Department service. When submitting at MeeSeva Center, you must bring a ₹2 Court Fee Stamp.
            </p>
          </div>
        </div>
      )}

      {/* How to Apply Section - NEW */}
      {service.steps && (
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-4">
          <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
            <ListOrdered className="w-4 h-4 text-blue-600" />
            How to Apply
          </h4>
          <ol className="space-y-2">
            {service.steps.en.map((step, idx) => (
              <li key={idx} className="text-sm text-gray-700 flex items-start gap-2">
                <span className="font-bold text-telangana-primary min-w-[20px]">{idx + 1}.</span>
                <span>{step}</span>
              </li>
            ))}
          </ol>
        </div>
      )}

      {/* Required Documents - ENHANCED */}
      <div className="border-t border-gray-200 pt-4 mb-4">
        <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
          <FileText className="w-4 h-4" />
          Required Documents ({service.required_documents.length})
        </h4>
        <ul className="space-y-2">
          {service.required_documents.map((doc, idx) => (
            <li key={idx} className="text-sm text-gray-700 flex items-start gap-2">
              <span className="text-telangana-primary mt-1">📄</span>
              <div className="flex-1">
                <span className="font-medium">{doc.name.en}</span>
                {doc.mandatory && <span className="text-red-500 ml-1">*</span>}
              </div>
            </li>
          ))}
        </ul>
      </div>

      {/* Important Notes Section - NEW */}
      {service.important_notes && (
        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-4">
          <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
            <Info className="w-4 h-4 text-yellow-600" />
            Important Notes
          </h4>
          <ul className="space-y-2">
            {service.important_notes.en.map((note, idx) => (
              <li key={idx} className="text-sm text-gray-700 flex items-start gap-2">
                <span className="text-yellow-600 mt-0.5">⚠️</span>
                <span>{note}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Source & Verification Section - NEW */}
      {service.source_verification && (
        <div className="bg-gray-50 border border-gray-200 rounded-lg p-3 mb-4">
          <div className="flex items-center gap-2 text-xs text-gray-600">
            <Shield className="w-3 h-3" />
            <div className="flex-1">
              <span className="font-medium">Source:</span> {service.source_verification.source}
              <span className="mx-2">•</span>
              <span className="font-medium">Last Verified:</span> {new Date(service.source_verification.last_verified).toLocaleDateString('en-IN', {
                day: 'numeric',
                month: 'short',
                year: 'numeric'
              })}
            </div>
          </div>
        </div>
      )}

      {/* Action Button */}
      {service.submission_modes.online.available && (
        <div className="pt-4 border-t border-gray-200">
          <a
            href={service.submission_modes.online.portal_url}
            target="_blank"
            rel="noopener noreferrer"
            className="block w-full bg-telangana-primary hover:bg-telangana-accent text-white font-semibold py-3 px-4 rounded-lg text-center transition-colors"
          >
            Apply Online →
          </a>
        </div>
      )}
    </div>
  )
}

// Made with Bob

